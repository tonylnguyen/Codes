from sklearn.svm import SVC
from sklearn import metrics
"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("/Users/tonynguyen/Desktop/ud120-projects/tools/")
from email_preprocess import preprocess
import numpy as np
import matplotlib.pyplot as plt


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

fsmall_train = features_train[:len(features_train)/100]
lsmall_train = labels_train[:len(labels_train)/100]

clf = SVC(kernel = 'rbf', C = 10000)

#kernel changes how the data is seperated
    #rbf is more scwiggly
    #linear is a straigh linear
# C is how smooth the line is the higher it is the more scwiggly

clf.fit(features_train, labels_train)


pred = clf.predict(features_test)
elements = range(1,1700)
counter = 0
for i in pred:
    if i == 1:
        counter = counter + 1

print counter

# print metrics.accuracy_score(labels_test, pred)

# c_score = [10, 100, 1000,  10000]
# for n in c_score:
#     clf = SVC(kernel='rbf', C = n)
#     clf.fit(fsmall_train, lsmall_train)
#     pred = clf.predict(features_test)
#     print metrics.accuracy_score(labels_test, pred)
