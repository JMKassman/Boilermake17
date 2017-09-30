from app import app
from flask import render_template
from pymongo import *
from app import mongo_setup

db = mongo_setup.client.Boilermake17
collection = db.main

#collection.insert_one({"name":"Test Person"})

test = []

for element in collection.find():
    test.append(element['name'])

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', name=test[0])
