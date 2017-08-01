from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
sys.path.append("/Users/tonynguyen/Desktop/ud120-projects/choose_your_own/")
import numpy as np
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels


features_train, labels_train, features_test, labels_test = makeTerrainData()


estimators = [10,35,50,100,200,500]
lrate = [1,2,5,10,25]

for i in estimators:
    print i
    boost = AdaBoostClassifier(n_estimators = i, learning_rate = 1)
    boost.fit(features_train, labels_train)
    pred = boost.predict(features_test)
    print metrics.accuracy_score(labels_test, pred)


#with smalls, 82%
#with bigs, 95%
