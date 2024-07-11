# AI-Based Car Part Recommendation System

## Summary
This recommendation system is designed to provide car part recommendations based on a given keyword (e.g., a specific part name, car make, or year). The system leverages a dataset containing car parts information, which includes year, make, part name, and part name image. The dataset is stored in a MySQL database, and the recommendations are generated using TF-IDF vectorization and cosine similarity. The system is implemented as a REST API using Flask, allowing users to obtain recommendations via HTTP GET requests.


## Overview
The car part recommendation system provides personalized suggestions based on user inputs, such as car make, year, or part name. This recommendation system employs a content-based filtering approach, leveraging TF-IDF vectorization and cosine similarity to generate recommendations.

## Recommendation System Types
There are two primary types of recommendation systems:

### Collaborative Filtering:

User-Based: Recommends items based on the preferences of similar users.
Item-Based: Recommends items similar to those a user has liked in the past.
Pros: Leverages user interactions and can discover new interests.
Cons: Requires a large amount of user data and can struggle with new users/items ("cold start" problem).

### Content-Based Filtering:

Recommends items similar to those a user has interacted with, based on item features.
Uses item metadata and user preferences.
Pros: Works well with few users and new items, and provides personalized recommendations based on item characteristics.
Cons: Limited to recommending items similar to those already interacted with and doesn't capture user behavior patterns well.
Content-Based Filtering with TF-IDF Vectorization
This system uses a content-based filtering approach due to its efficiency with textual data and flexibility with new users/items. Specifically, it utilizes:

### TF-IDF Vectorization:

Term Frequency-Inverse Document Frequency (TF-IDF): A statistical measure used to evaluate the importance of a word in a document relative to a collection of documents (corpus).
Converts textual data (e.g., car make, year, part name) into numerical vectors that represent the importance of each term.

### Cosine Similarity:

Measures the cosine of the angle between two non-zero vectors.
Determines the similarity between the input keyword vector and car parts vectors.
Outputs a similarity score indicating how closely related the items are.


### AI-Based Recommendation Logic:

Combine the text features (year, make, part name) into a single string.
Use TF-IDF to convert the combined text data into numerical vectors.
Compute the cosine similarity between the keyword vector and the car parts vectors.
Identify and return the most similar car parts based on the computed similarities.


## System Components

### Key Components
MySQL Database: Stores the car parts information in a table tbl_parts.
Pandas: Used for data manipulation and loading data from the MySQL database.
TF-IDF Vectorizer: Converts text data into numerical vectors for similarity comparison.
Cosine Similarity: Measures the similarity between the keyword and the car parts data.
Flask: Provides the REST API endpoint for the recommendation system.
Pillow: Generates images for each part name, which are included in the dataset.
Steps to Build the System


### MySQL Database:

Create a MySQL database and a table named tbl_parts with columns for year, make, part name, and part name image.


### Data Preparation:

Generate a CSV file or data in part_name table containing combinations of years, makes, and part names.
Create images for each part name and save them in a directory.
Update the image paths and load it into the MySQL table tbl_parts.

### Flask REST API:

Provides an endpoint /recommend for obtaining recommendations based on a keyword.
Connects to the MySQL database and loads car parts data.
Preprocesses the data by combining text features for vectorization.
Generates recommendations using TF-IDF vectorization and cosine similarity.
Returns the recommendations as a JSON response.
