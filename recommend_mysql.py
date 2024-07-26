import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Blueprint, request, jsonify
from PIL import Image, ImageDraw, ImageFont
import mysql.connector
import os

recommend_mysql_blueprint = Blueprint('recommend_mysql', __name__)



def connect_to_db():
    """Connect to the MySQL database."""
    return mysql.connector.connect(
        host="localhost",  # e.g., "localhost"
        user="root",  # e.g., "root"
        password="",
        database="autoparts"
    )

def load_data_from_db():
    """Load data from MySQL database into a pandas DataFrame."""
    db_connection = connect_to_db()
    query = """SELECT p.product_id as id, p.name, p.image1, p.image2, p.our_price as ourPrice, p.description, m.name as make, p.`year`, c.name as part_name
               FROM product p
               inner join make m on m.make_id =p.make_id
               inner join category c on c.category_id = p.category_id """

    data = pd.read_sql(query, db_connection)
    db_connection.close()
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
data = load_data_from_db()

@recommend_mysql_blueprint.route('/recommend', methods=['GET'])
def recommend_endpoint():
    keyword = request.args.get('keyword', '')
    if not keyword:
        return jsonify({"error": "Keyword parameter is required"}), 400

    recommendations = recommend(data, keyword)
    return recommendations.to_json(orient='records')
