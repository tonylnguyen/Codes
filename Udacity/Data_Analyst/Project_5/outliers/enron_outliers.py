#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_5/ud120-projects/tools")
from feature_format import featureFormat, targetFeatureSplit
import numpy


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_5/ud120-projects/final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

dlist = []

# print data
### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    # matplotlib.pyplot.scatter( salary, bonus )
    row = (salary, bonus)
    dlist.append(row)

dlist = sorted(dlist, reverse = True)
dlist.pop(0)

for point in dlist:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )



matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
