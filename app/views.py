from app import app
from flask import render_template, flash, redirect, request
from pymongo import *
from app import mongo_setup
from .ScheduleCreator import ScheduleCreator
from .NameInput import NameInput

baseAvailabilityArray = []

for i in range(288):
    baseAvailabilityArray.append(True)

# @param: name - name of person to update
# @param: classes - array of classes for a person
# @param: freeArray - array of free time slots
def modifyFreeArray(name, classes, freeArray):
    freeArray = baseAvailabilityArray
    #TODO find out why the array data is persisting and remove the above line
    for element in classes:
        print(element)
        start = element['start_time'] // 5
        end = element['end_time'] // 5
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
        tmp0 = ""
        tmp1 = ""
        hour0 = arr[0][i] // 60
        minute0 = arr[0][i] % 60
        hour1 = arr[1][i] // 60
        minute1 = arr[1][i] % 60 + 5
        if minute0 == 60:
            hour0 = hour0 + 1
            minute0 = 0
        if minute1 == 60:
            hour1 = hour1 + 1
            minute1 = 0
        if hour0 == 0 and minute0 == 0:
            tmp0 = "00:00"
        elif hour0 == 0:
            tmp0 = "00:" + str(minute0)
        elif minute0 == 0:
            tmp0 = str(hour0) + ":00"
        else:
            tmp0 = str(hour0) + ":" + str(minute0)

        if hour1 == 0 and minute1 == 0:
            tmp1 = "00:00"
        elif hour1 == 0:
            tmp1 = "00:" + str(minute1)
        elif minute1 == 0:
            tmp1 = str(hour1) + ":00"
        else:
            tmp1 = str(hour1) + ":" + str(minute1)
        str0 = str0 + tmp0 + " - " +  tmp1 + ", "
    return str0[:-2]

db = mongo_setup.client.Boilermake17
collection = db.main

#output = convertCalculatedArrayToReadableTimes(calculateFreeTime(compareFreeArrays(FreeArray0, FreeArray1)))

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = NameInput(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        name1 = form.name1.data
        name2 = form.name2.data
        test = []
        cursor = collection.find({'$or': [{'name':name1},{'name':name2}]})
        for element in cursor:
            test.append(element)
        if len(test) >= 2:
            schedule0 = test[0]['Schedule']
            FreeArray0 = test[0]['FreeTime']

            schedule1 = test[1]['Schedule']
            FreeArray1 = test[1]['FreeTime']

            output = convertCalculatedArrayToReadableTimes(calculateFreeTime(compareFreeArrays(FreeArray0, FreeArray1)))
        else:
            output = "Something went wrong. One or both of the names entered did not match an entry"
        return render_template('index.html', output=output, title='Schedule Comparison', form=form)
    return render_template('index.html', output="", title='Schedule Comparison', form=form)

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = ScheduleCreator(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        flash('Document has been created')
        name = form.name.data
        course1 = form.course1.data
        start_time1 = form.start_time1.data
        end_time1 = form.end_time1.data
        course2 = form.course2.data
        start_time2 = form.start_time2.data
        end_time2 = form.end_time2.data
        course3 = form.course3.data
        start_time3 = form.start_time3.data
        end_time3 = form.end_time3.data
        course4 = form.course4.data
        start_time4 = form.start_time4.data
        end_time4 = form.end_time4.data
        course5 = form.course5.data
        start_time5 = form.start_time5.data
        end_time5 = form.end_time5.data
        document = {'name':name, 'Schedule': {'Monday': [{'course': course1, 'start_time': start_time1, 'end_time': end_time1}, {'course': course2, 'start_time': start_time2, 'end_time': end_time2}, {'course': course3, 'start_time': start_time3, 'end_time': end_time3}, {'course': course4, 'start_time': start_time4, 'end_time': end_time4}, {'course': course5, 'start_time': start_time5, 'end_time': end_time5}]}, 'FreeTime': baseAvailabilityArray}
        collection.insert(document)
        schedule = document['Schedule']
        courses = schedule['Monday']
        freeTime = document['FreeTime']
        modifyFreeArray(name, courses, freeTime)
        return redirect('/index')
    return render_template('create.html', title='Schedule Creator', form=form)
