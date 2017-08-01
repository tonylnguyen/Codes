#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_5/ud120-projects/final_project/final_project_dataset.pkl", "r"))
count = 0
count2 = 0
# for k, v in enron_data.iteritems():
#     if k == 'LAY KENNETH L' or k == 'SKILLING JEFFREY K' or k == 'FASTOW ANDREW S':
#         for key, value in v.iteritems():
#             if key == 'total_payments':
#                 print k, value

for k, v in enron_data.iteritems():
    if v['total_payments'] == 'NaN':
        count = count + 1

print count
