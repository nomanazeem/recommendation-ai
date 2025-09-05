#pip install Flask mysql-connector-python pandas scikit-learn


import pandas as pd
import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, jsonify

app = Flask(__name__)

def connect_to_db():
    """Connect to the MySQL database."""
    return mysql.connector.connect(
        host="your_host",  # e.g., "localhost"
        user="your_user",  # e.g., "root"
        password="your_password",
        database="your_database"
    )

def load_data_from_db():
    """Load data from MySQL database into a pandas DataFrame."""
    db_connection = connect_to_db()
    query = "SELECT * FROM tbl_parts"
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
    similar_indices = cosine_sim[0].argsort()[-10:][::-1]

    # Return the most similar items
    return data.iloc[similar_indices]

@app.route('/recommend', methods=['GET'])
def recommend_endpoint():
    keyword = request.args.get('keyword', '')
    if not keyword:
        return jsonify({"error": "Keyword parameter is required"}), 400

    data = load_data_from_db()
    recommendations = recommend(data, keyword)
    return recommendations.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
