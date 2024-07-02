import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv('datasource.csv')
movies = data[['id', 'title','overview','genre']]
movies['tags'] = movies['overview']+movies['genre']

new_data = movies[['id','title', 'tags']]
#print(new_data)

cv = CountVectorizer(max_features=10000, stop_words='english')
#print(cv)

vector = cv.fit_transform(new_data['tags'].values.astype('U')).toarray()
#print (vector.shape)

similarity = cosine_similarity(vector)
#print (similarity)

#distance = sorted(list(enumerate(similarity[2])), reverse=True, key=lambda vector:vector[1])
#distance5 = distance[0:5]
#print(distance5)

#def recommend(movie):
#    index = new_data[new_data['title']==movie].index[0]
#    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
#    for i in distance[0:5]:
#        print(new_data.iloc[i[0]].title)

#recommend("Iron Man")

import pickle
pickle.dump(new_data, open('.resources/movies_list.pkl', 'wb'))
pickle.dump(similarity, open('.resources/similarity.pkl', 'wb'))

#movies = pickle.load(open('movies_list.pkl', 'rb'))
#print(movies)
