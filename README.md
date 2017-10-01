# Boilermake17

## Introduction

 This webapp has two pages. The first page allows a user to input two names and see all time periods where both people are free. This works by querying the mongo database to find the 2 people's schedules and compares them. The second page allows a user to input their schedule and save it to the mongo database

 ## Running this on your own system

 ### installed dependencies in python venv:

 (venv should be located in folder called _flask_ in the root directory of the project)

 1. flask
 2. flask-wtf
 3. pymongo[tls]

The Installing Flask section on [this page](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) is very helpful

 There are 2 files required that are not on GitHub because they contain private information. These 2 files are called _config.py_ and _mongo_setup.py_

 The _config.py_ file should look like this, with the secret key replaced

 ```python
 CSRF_ENABLED = True
 SECRET_KEY = 'this-is-just-a-random-string'
 ```

 The _mongo_setup.py_ file is used to setup the initial connection to a mongo database. The file should look like this if using mongodb atlas. The only requirement is that a client variable is created that points to a mongo database

 ```python
 from pymongo import *
 client = MongoClient("Replace-with-mongo-db-atlas-URI-connection-string")
```
