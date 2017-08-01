#!/usr/bin/env python
import pymongo
import json

client = pymongo.MongoClient('mongodb://127.0.0.1:27017') # remember to have the instance of mongodb running
my_file = '/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_3/Project_3/sample.json'

db = client.test #this tells mongo to use the test data base
collections = db.sample # this tells mongo to create/use the project_3 collections

#insert into mongodb
with open(my_file, 'r') as data:
    parse = json.loads(data.read())
    for item in parse:
        collections.insert(item)
