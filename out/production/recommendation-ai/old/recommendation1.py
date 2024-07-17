import pandas as pd

def load_csv(file_path):
    """Load CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)

def recommend(data, keyword):
    """Recommend car parts based on the given keyword."""
    keyword = keyword.lower()
    filtered_data = data[
        data.apply(lambda row: keyword in str(row['year']).lower() or
                                 keyword in row['make'].lower() or
                                 keyword in row['part_name'].lower(), axis=1)
    ]
    return filtered_data

# Load the CSV file
file_path = 'car_parts.csv'
data = load_csv(file_path)

# Example usage
keyword = 'Toyota Oil filter'  # You can change this to any keyword like 'air filter' or '2012'
recommendations = recommend(data, keyword)

# Display recommendations
print(recommendations)
