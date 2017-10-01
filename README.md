# Boilermake17

## installed dependencies in python venv:

(venv should be located in folder called _flask_ in the root directory of the project)

1. flask
2. flask-wtf
3. pymongo[tls]

This webapp has two pages. The first page allows a user to input two names and see all time periods where both people are free. This works by querying the mongo database to find the 2 people's schedules and compares them. The second page allows a user to input their schedule and save it to the mongo database
