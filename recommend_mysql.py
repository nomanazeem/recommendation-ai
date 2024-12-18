import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Blueprint, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont
import mysql.connector
import os

recommend_mysql_blueprint = Blueprint('recommend_mysql', __name__)
load_dotenv()

def get_gemini_api():
    try:
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        model = genai.GenerativeModel('gemini-pro')
        return model
    except Exception as e:
         print(f"error during setup genmai api: {e}")
         return None

def connect_to_db():
    """Connect to the MySQL database."""
    return mysql.connector.connect(
        host="localhost",  # e.g., "localhost"
        user="root",  # e.g., "root"
        password="root",
        database="autoparts"
    )

def generate_product_description(gemini_model, product_data):
    """Generates a product description using Gemini API.

    Args:
      product_data (dict): A dictionary containing the product information.
    """

    if not gemini_model:
        return "Gemini model is not initialized, can't generat description"
    prompt = f"""Generate a concise and appealing product description for a car part with following details:
                 Make: {product_data['make']},
                 Part: {product_data['part_name']},
                 Year: {product_data['year']},
                 Price: {product_data['ourPrice']}
                """
    try:
       response = gemini_model.generate_content(prompt)
       return response.text
    except Exception as e:
       print(f"error while generate description {e}")
       return "Error generating the description"


def load_data_from_db_with_descriptions(limit =20):
    """Loads product data from the database and generates descriptions with Gemini API."""

    db_connection = connect_to_db()
    if not db_connection:
         return None

    query = """SELECT p.product_id as id, p.name, p.image1, p.image2, p.our_price as ourPrice, p.description, m.name as make, p.`year`, c.name as part_name
               FROM product p
               inner join make m on m.make_id =p.make_id
               inner join category c on c.category_id = p.category_id 
               LIMIT %s"""

    data = pd.read_sql(query, db_connection, params=(limit,))
    db_connection.close()

    # Initialize the Gemini model
    gemini_model = get_gemini_api()


    if gemini_model:
       data["description"] = data.apply(
          lambda row: generate_product_description(
              gemini_model,
                  {
                      "make": row["make"],
                      "year": row["year"],
                      "part_name": row["part_name"],
                      "ourPrice": row["ourPrice"]
                  },
              ) ,
              axis=1
           )


    return data



def preprocess_data(data):
    """Combine the text features for TF-IDF vectorization."""
    data['Combined'] = data['year'].astype(str) + ' ' + data['make'] + ' ' + data['part_name']
    return data


def recommend(data, keyword):
    """Recommend car parts based on the given keyword using TF-IDF and cosine similarity."""
    keyword = keyword.lower()

    # Combine the text features
    data = preprocess_data(data)
    print(data);


    # Vectorize the text data
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(data['Combined'])

    # Vectorize the keyword
    keyword_tfidf = vectorizer.transform([keyword])

    # Compute cosine similarity
    cosine_sim = cosine_similarity(keyword_tfidf, tfidf_matrix)

    # Get the indices of the most similar items
    # get top 10
    similar_indices = cosine_sim[0].argsort()[-11:][::-1][1:]

    # Return the most similar items
    return data.iloc[similar_indices]

# Load
data = load_data_from_db_with_descriptions()

@recommend_mysql_blueprint.route('/recommend', methods=['GET'])
def recommend_endpoint():
    keyword = request.args.get('keyword', '')
    if not keyword:
        return jsonify({"error": "Keyword parameter is required"}), 400

    recommendations = recommend(data, keyword)
    return recommendations.to_json(orient='records')

