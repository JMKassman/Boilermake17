from app import app
from flask import render_template
from pymongo import *
from app import mongo_setup

# @param: name - name of person to update
# @param: classes - array of classes for a person
# @param: freeArray - array of free time slots
def modifyFreeArray(name, classes, freeArray):
    for element in classes:
        print(element)
        start = element['start_time'] / 5
        end = element['end_time'] / 5
        print(start)
        print(end)
        for i in range(len(freeArray)):
            if i >= start and i < end:
                freeArray[i] = False
                print("Value updated")
        collection.update({'name':name},{'$set':{'FreeTime':freeArray}})
        print("collection updated")

def compareFreeArrays(arr1, arr2):
    arr3 = []
    for i in range(len(arr1)):
        arr3.append((arr1[i] == True and arr2[i] == True))
    return arr3

# @param arr - array of free times of both people generated from compareFreeArrays()
def calculateFreeTime(arr):
    free = []
    for i in range(len(arr)):
        if arr[i] == True:
            free.append(i*5)
    start = []
    end = []
    for i in range(len(free)):
        if i == 0:
            start.append(free[i])
        if i > 0 and free[i] != free[i-1]+5:
            start.append(free[i])
        if i < len(free)-1 and free[i] != free[i+1]-5:
            end.append(free[i])
        if i == len(free)-1:
            end.append(free[i])
    return [start, end]

def convertCalculatedArrayToReadableTimes(arr):
    str0 = "Time when both people are free: "
    length = len(arr[0])
    for i in range(length):
        tmp0 = str(arr[0][i] // 60) + ":" + str(arr[0][i] % 60)
        tmp1 = str(arr[1][i] // 60) + ":" + str((arr[1][i] % 60) + 5)
        str0 = str0 + tmp0 + " - " +  tmp1 + ", "
    return str0[:-2]

db = mongo_setup.client.Boilermake17
collection = db.main

test = []

cursor = collection.find()

for element in cursor:
    test.append(element)

schedule0 = test[0]['Schedule']
monday0 = schedule0["Monday"]
FreeArray0 = test[0]['FreeTime']

schedule1 = test[1]['Schedule']
monday1 = schedule1["Monday"]
FreeArray1 = test[1]['FreeTime']

output = convertCalculatedArrayToReadableTimes(calculateFreeTime(compareFreeArrays(FreeArray0, FreeArray1)))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', output=output, title='Schedule Comparison')
