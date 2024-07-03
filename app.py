import pandas as pd
import json

data = pd.read_csv('autoparts.csv')
#import sys
#print(sys.executable)

from flask import request

from flask import Flask
app = Flask(__name__)

import pickle

autoparts = pickle.load(open(".resources/autoparts_list.pkl", 'rb'))
autoparts_similarity = pickle.load(open(".resources/autoparts_similarity.pkl", 'rb'))

@app.route('/')
def index():
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


    found=False

    #Part name
    if(found==False):
        print("Searching part name...")
        findElement = autoparts[autoparts['part_name'] == keyword]
        if(findElement.empty==True):
            print("Error: part name not found...")
            found=False
        else:
            found=True

    #Make
    if(found==False):
        print("Searching make...")
        findElement = autoparts[autoparts['make'] == keyword]
        if(findElement.empty==True):
            print("Error: make name not found...")
            found=False
        else:
            found=True

    #Year
    if(found==False and keyword.isnumeric()):
        print("Searching year...")
        findElement = autoparts[autoparts['year'] == int(keyword)]
        if(findElement.empty==True):
            print("Error: year not found...")
            found=False
        else:
            found=True

    if(found==False):
        print("Not found....")
        response = {
                        "data": [],
                        "status": 'false',
                        "message": 'No data found'
                    }
        return response


    index = findElement.index[0]
    #print(len(findMovie))

    #index = findMovie.index[0]

    #print("index is:"+index)
    #return -1
    #print(similarity[index])
    distance = sorted(list(enumerate(autoparts_similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_list = []
    for i in distance[0:11]:
        recommendObject = autoparts.iloc[i[0]]

        #recommend_list.append(str(recommendObject.year) + " "+ str(recommendObject.make) + " "+ str(recommendObject.part_name))
        recommend_list.append(str(recommendObject.description))
        response = {
                        "data": recommend_list,
                        "status": 'true',
                        "message": 'Success matched'
                    }

    return response