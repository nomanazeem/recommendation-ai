import pandas as pd

data = pd.read_csv('datasource.csv',nrows=10)
#import sys
#print(sys.executable)

from flask import request

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Welcome recommendation system</h1>"


@app.route('/recommend/')
def recommend():
    keyword = request.args.get('keyword')

    print (data)
    print ("\n\n")
    return "Hi Noman you searching for ...\n"+keyword
