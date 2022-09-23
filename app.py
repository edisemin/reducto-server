from flask import Flask, request, jsonify
import os
import subprocess as sp
from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
from users import user_schema

load_dotenv()
mongopass = os.getenv('mongopass')
ca = certifi.where()

client = MongoClient(mongopass, tlsCAFile=ca)
db = client.reducto
coll = db.users


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "hello, welcome to reducto server"

@app.route('/users/', methods=['GET'])
def get_users():
    collection = coll.find()
    for user in collection:
        print(user['name'])
    
    return "showing all users"

@app.route('/dashboard/', methods=['GET'])
def dashboard():
    date = sp.getoutput("date /t")
    return date

# Not finished
@app.route('/login/', methods=['POST'])
def login():
    return "thanks for logging in"

# Not finished
@app.route('/register/', methods=['POST'])
def register():
    username = request.form['username']
    bname = request.form['bname']
    user_schema["username"] = username
    user_schema["businessname"] = bname
    coll.insert_one(user_schema)
    return "Thanks for registering"

# Not finished
@app.route('/form/', methods=['PUT'])
def form():
    return "thanks for letting us know about your co2"


if __name__ == '__main__':
    app.run(debug=True)
