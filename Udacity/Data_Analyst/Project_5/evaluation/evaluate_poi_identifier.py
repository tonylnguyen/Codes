#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""
import os
os.chdir('/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_5/ud120-projects/validation')

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

from sklearn import tree
from sklearn import metrics


### your code goes here

from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels,test_size=0.3, random_state=42)
clf = clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)
# How many POIs are predicted for the test set for your POI identifier?
count = []
for i in labels_test:
    if i == 1:
        count.append(i)

# print len(count)

# How many people total are in your test set?
# print len(labels_test)

#If your identifier predicted 0. (not POI)
#for everyone in the test set, what would its accuracy be?
# 29/33

#Look at the predictions of your model and compare them to the
#true test labels. Do you get any true positives?

# for i,v in enumerate(pred):
#     if v == 1:
#         print i

# for i,v in enumerate(labels_test):
#     if v == 1:
#         print i

# I printed the index for 1s and compared the two. If there are any matches,
# then there is a true positive (in this case there is no true positive)

#even with a 77% accuracy, we got no matches
# what are the precision_score and recall_score
prec = metrics.precision_score(labels_test, pred)
recall = metrics.recall_score(labels_test, pred)
# print prec, recall


predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

t = metrics.confusion_matrix(true_labels, predictions)
print t

# true negative, false positives
# false negatives, true positives


# print metrics.precision_score(predictions, true_labels)
print metrics.recall_score(predictions, true_labels)
