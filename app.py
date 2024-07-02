import pandas as pd
import json

data = pd.read_csv('datasource.csv')
#import sys
#print(sys.executable)

from flask import request

from flask import Flask
app = Flask(__name__)

import pickle

movies_list = pickle.load(open("resources/movies_list.pkl", 'rb'))
similarity = pickle.load(open("resources/similarity.pkl", 'rb'))

@app.route('/')
def index():
    movies = data[['id', 'title','overview','genre']]
    print(movies)
    return "<h1>Welcome recommendation system</h1>"




@app.route('/recommend/')
def recommend():
    keyword = request.args.get('keyword')
    if(keyword == ''):
        response = {
                "data": [],
                "status": 'false',
                "message": 'No data found'
            }
        return response


    findMovie = movies_list[movies_list['title'] == keyword]
    #print(findMovie)
    if(findMovie.empty==True):
        response = {
                        "data": [],
                        "status": 'false',
                        "message": 'No data found'
                    }
        return response

    index = findMovie.index[0]
    #print(len(findMovie))

    #index = findMovie.index[0]

    #print("index is:"+index)
    #return -1
    #print(similarity[index])
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_list = []
    for i in distance[1:11]:
        recommend_list.append(movies_list.iloc[i[0]].title)

        response = {
                        "data": recommend_list,
                        "status": 'true',
                        "message": 'Success matched'
                    }

    return response