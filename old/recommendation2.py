import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_csv(file_path):
    """Load CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)

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

# Load the CSV file
file_path = 'car_parts.csv'
data = load_csv(file_path)

# Example usage
keyword = '2015 Taillight'  # You can change this to any keyword like 'air filter' or '2012'
recommendations = recommend(data, keyword)

# Display recommendations
print(recommendations)
