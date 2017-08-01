#!/usr/bin/python

from sklearn import tree
from sklearn import metrics


"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.
    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("/Users/tonynguyen/Desktop/ud120-projects/tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#min_samples_split is the amount of observations needed to split into a new tree

#########################################################
clf = tree.DecisionTreeClassifier(min_samples_split = 40)
clf.fit(features_train, labels_train)

print features_train.shape
pred = clf.predict(features_test)
#
print metrics.accuracy_score(labels_test, pred)

#########################################################
