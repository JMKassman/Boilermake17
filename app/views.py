from app import app
from flask import render_template
from pymongo import *
from app import mongo_setup

client = mongo_setup.client.Boilermake17
db = client.Boilermake17

cursor = db.main.find()
for document in cursor:
    myUsers=['name']

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', name=)
