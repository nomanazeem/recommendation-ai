import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv('autoparts.csv')
autoparts = data[['year', 'make','part_name','description']]
#print(autoparts)

cv = CountVectorizer(max_features=10000, stop_words='english')
#print(cv)

vector = cv.fit_transform(autoparts['description'].values.astype('U')).toarray()
#print (vector.shape)

similarity = cosine_similarity(vector)
#print (similarity)

import pickle
pickle.dump(autoparts, open('.resources/autoparts_list.pkl', 'wb'))
pickle.dump(similarity, open('.resources/autoparts_similarity.pkl', 'wb'))
