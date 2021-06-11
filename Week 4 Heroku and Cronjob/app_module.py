from flask import Flask

app = Flask(__name__)

# commit 1
@app.route('/')
def home():
    return 'This is my homepage for film'

# commit 2   
@app.route('/hello')
def hello():
    return {"message": "Hello this is my API deployed on heroku"}

if __name__ == "__main__":
    app.run(debug=True)