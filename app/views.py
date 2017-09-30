from app import app
from flask import render_template
import pymongo
from app import mongo_setup

db = mongo_setup.client.Boilermake17

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', name=)
