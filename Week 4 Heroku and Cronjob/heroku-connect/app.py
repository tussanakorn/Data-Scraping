from flask import Flask, jsonify
import pymongo


def connect_to_database():
    # ใช้ os.environ แทน ไม่ควร hard code อะไรที่เป็น credential
    MONGODB_URI = 'mongodb://heroku_672rlh8s:s18fo4q6ejpm67lmodcn4hqjil@ds161551.mlab.com:61551/heroku_672rlh8s'
    client = pymongo.MongoClient(MONGODB_URI, retryWrites=False)
    db = client['heroku_672rlh8s']
    collection_name = 'covid_stats'
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
    collection = db[collection_name]
    return collection

app = Flask(__name__)
collection = connect_to_database()

@app.route('/')
def home():
    cursor = collection.find({}, projection={"_id": 0})
    documents = [document for document in cursor]
    return jsonify(documents)
    

if __name__ == "__main__":
    app.run()