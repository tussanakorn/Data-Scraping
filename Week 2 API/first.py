from flask import Flask , jsonify , request
import json 
import pandas as pd
from pymongo import MongoClient

def connection_database():
    #connectdatabase -> collection
    URI = 'mongodb+srv://user02:12345@cluster0-j2ism.mongodb.net/test' #URI ใน MongoDB
    client = MongoClient(URI)
    #เข้าถึง database ใน cluster
    db = client.sample_mflix 
    collection = client['sample_mflix']['movies']
    return collection
   

app = Flask(__name__)
collection_f = connection_database()

@app.route('/film')
def home():
    documents = []
    query = {}
    cursor = collection_f.find(query)
    for doc in cursor:
        documents.append(doc)
    return jsonify(documents)

@app.route('/film1')
def home2():
    documents = []
    years = request.args.get('year' , type = int)
    query = {'year' : years}
    cursor = collection_f.find(query)

    for doc in cursor:
        documents.append(doc)
    return jsonify(documents)

    

if __name__ == '__main__':
    app.run(debug=True)