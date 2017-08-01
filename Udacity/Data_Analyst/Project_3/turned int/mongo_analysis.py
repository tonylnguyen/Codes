
# -*- coding: utf-8 -*-
#!/usr/bin/env python
import pymongo
import json
import pprint

client = pymongo.MongoClient('mongodb://127.0.0.1:27017') # remember to have the instance of mongodb running
menlo_json = '/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_3/Project_3/menlo.json'
sample_json = '/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_3/Project_3/sample.json'


def insert_to_mongo(my_file):
    """
    this imports the JSON file to mongo db
    use menlo_json or sample_json
    """
    with open(my_file, 'r') as data:
        parse = json.loads(data.read())
        for item in parse:
            collections.insert(item)

db = client.test #this tells mongo to use the test data base
collections = db.sample # this tells mongo to create/use the project_3 collections


db = client.test #this tells mongo to use the test data base
collections = db.project_3 # this tells mongo to create/use the project_3 collections
menlo = db.menlo # this is the main OSM data on Menlo Park,CA (via mongodb)
sample = db.sample # this is the sample file used to gather my data (via mongodb)


most_posts = [{'$group':{"_id":"$input_by.user",'count':{'$sum':1}}},{'$sort':{'count':-1}},{"$limit":10}]
city_count = [{'$group':{"_id":"$address.city",'count':{'$sum':1}}},{'$sort':{'count':-1}}]
find_city = [{'$match':{"address.city":"Redwood City"}}]
county = [{"$group":{"_id":"$details.county", "count":{"$sum":1}}},{'$sort':{'count':-1}},
          {"$limit":10}]

aggregation = menlo.aggregate(most_posts) # use the variables above to create a for loop
# remember to change the database (menlo or sample) and the parameters

# prints out the query defined by the aggregation variable
for i in aggregation:
    pprint.pprint(i)

def simple_stats(mongo_file):
    """
    This returns the total Documents, nodes, ways, and users that contributted
    """
    num_documents = mongo_file.find().count()
    num_nodes = mongo_file.find({'type':'node'}).count()
    num_way = mongo_file.find({'type':'way'}).count()
    users = len(mongo_file.distinct("input_by.user"))

    print num_documents, num_nodes, num_way, user
