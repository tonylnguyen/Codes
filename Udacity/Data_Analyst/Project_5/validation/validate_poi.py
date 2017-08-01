#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""
import os
os.chdir('/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_5/ud120-projects/validation')


import pickle
import sys
sys.path.append("/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_5/ud120-projects/tools")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_5/ud120-projects/final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!
from sklearn import tree
from sklearn import metrics


clf = tree.DecisionTreeClassifier()
clf.fit(features, labels)
pred = clf.predict(features)
print metrics.accuracy_score(labels, pred)

#splitting the data
from sklearn import cross_validation

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels,test_size=0.3, random_state=42)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print metrics.accuracy_score(labels_test, pred)
