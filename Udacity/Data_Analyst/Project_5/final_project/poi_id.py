#!/usr/bin/python
import os
# setting the working directory
os.chdir('/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_5/ud120-projects/final_project')

#importing all the libraries
import numpy
import sys
import pickle
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.pipeline import Pipeline
from sklearn import decomposition

"""
Task 1: Select what features you'll use.
features_list is a list of strings, each of which is a feature name.
The first feature must be "poi".
You will need to use more features
"""

ffeatures_list = ['poi', 'salary', 'bonus', 'total_stock_value',
                  'from_poi_to_this_person', 'from_this_person_to_poi', 'expenses',
                  'long_term_incentive']

# Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)
my_dataset = data_dict
# note: there are 146 objects (people) in my_dataset

"""
# Task 2: Remove outliers
"""

def nan_search(data):
    """
    This function gives me a count of all the features that has a NaN value.
    This will help be decide which features to use for the classifier, by
    choose features with little NaN values.
    """
    no_info = {}
    test = []
    for k, v in data.iteritems():
        for key, value in v.iteritems():
            if value == 'NaN':
                test.append(key)

    for i in test:
        if i not in no_info:
            no_info[i] = 0

        if i in no_info:
            no_info[i] += 1

    return no_info

no_info = nan_search(my_dataset)
# for k,v in no_info.items():
#     print k, v

def computeFraction(poi_messages, all_messages):
    """
    Used with features_creater to find the ratio of messages to POI.
    Taken from the mini project in lesson 12.4
    """
    fraction = 0.

    if poi_messages != 0:
        fraction = float(poi_messages) / float(all_messages)

    return fraction


def features_creater(data):
    """
    this section removes any outliers and set NaN Values to 0
    """

    del data['TOTAL']

    for key, value in data.iteritems():
        for k, v in value.iteritems():
            if v == "NaN":
                v = 0
            value[k] = v

    """
    Taken from the mini project in lesson 12.4
    It takes the emailed messages and
    find the ratio of those emails that were sent to POI
    """
    for name, value in data.iteritems():

        data_point = data[name]

        from_poi_to_this_person = data_point["from_poi_to_this_person"]
        to_messages = data_point["to_messages"]
        fraction_from_poi = computeFraction(
            from_poi_to_this_person, to_messages)
        data_point["fraction_from_poi"] = fraction_from_poi

        from_this_person_to_poi = data_point["from_this_person_to_poi"]
        from_messages = data_point["from_messages"]
        fraction_to_poi = computeFraction(
            from_this_person_to_poi, from_messages)
        data_point["fraction_to_poi"] = fraction_to_poi

    return data

my_dataset = features_creater(my_dataset)

"""
Task 3: Create new feature(s): This list uses the fraction of emails.
"""
# After review the data provided by FindLaw, these are the features I decided
# to use

features_list = ['poi', 'salary', 'bonus', 'total_stock_value',
                 'fraction_to_poi', 'fraction_from_poi', 'expenses',
                 'long_term_incentive', 'total_payments','restricted_stock',
                 'exercised_stock_options']


def feature_returner(data):
    """
    Returns a new data with features defined by features_list
    """

    for names, values in data.items():
        for k, v in values.items():
            if k not in features_list:
                del values[k]

    return data


# Store to my_dataset for easy export below.
my_dataset = feature_returner(my_dataset)

# Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys=True)
labels, features = targetFeatureSplit(data)

# Scales the features for classifiers
mms = MinMaxScaler(feature_range=(0, 1))
mms_scale = mms.fit_transform(features)

"""
# Task 4: Try a varity of classifiers
# Please name your classifier clf for easy export below.
# Note that if you want to do PCA or other multi-stage operations,
# you'll need to use Pipelines. For more info:
# http://scikit-learn.org/stable/modules/pipeline.html
"""

# note: if you want to use scaled features, replace features with mms_scale
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)


def classifiers(features_train1, labels_train1, features_test1, labels_test1):

    """
    fits the data to multiple classifiers and prints the accuracy_score
    """

    clf_nb = GaussianNB()
    clf_nb.fit(features_train1, labels_train1)
    pred_nb = clf_nb.predict(features_test1)
    nb_score = metrics.accuracy_score(labels_test1, pred_nb)

    clf_kn = KNeighborsClassifier(n_neighbors=5)
    clf_kn.fit(features_train1, labels_train1)
    pred_kn = clf_kn.predict(features_test1)
    kn_score = metrics.accuracy_score(labels_test1, pred_kn)

    clf_svc = SVC(kernel='rbf')
    clf_svc.fit(features_train1, labels_train1)
    pred_svc = clf_svc.predict(features_test1)
    svc_score = metrics.accuracy_score(labels_test1, pred_svc)

    clf_tree = DecisionTreeClassifier()
    clf_tree.fit(features_train1, labels_train1)
    pred_tree = clf_tree.predict(features_test1)
    tree_score = metrics.accuracy_score(labels_test1, pred_tree)

    clf_kmeans = KMeans()
    clf_kmeans.fit(features_train1, labels_train1)
    pred_kmeans = clf_kmeans.predict(features_test1)
    kmeans_score = metrics.accuracy_score(labels_test1, pred_kmeans)

    print "NB Score: ", nb_score
    print "KN Score: ", kn_score
    print "SVC Score:", svc_score
    print "Tree score:", tree_score
    print "kMeans score:", kmeans_score

# to see the score, uncomment the line below
# classifiers(features_train, labels_train, features_test, labels_test)

"""
# Task 5: Tune your classifier to achieve better than .3 precision and recall
# using our testing script. Check the tester.py script in the final project
# folder for details on the evaluation method, especially the test_classifier
# function. Because of the small size of the dataset, the script uses
# stratified shuffle split cross validation. For more info:
# http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html
"""


## Example starting point. Try investigating other evaluation techniques!
## Note: to save processing time, I commented out the unused classifiers.
##       please uncomment the lines if you wish to see the results.

"""
KNeighbors
"""

## This loop seeks which value n_neighbors is best. Prints out all 4 metric
## scores (accuracy_score, F1, recall_score, precision_score)

# for i in range(1, 100):
#     clf = KNeighborsClassifier(n_neighbors=3, weights='uniform', leaf_size = i)
#     clf.fit(features_train, labels_train)
#     pred_kn = clf.predict(features_test)
#     kn_score = metrics.accuracy_score(labels_test, pred_kn)
#     """
#     using this loop to see what the best value for n_neighbors will be.
#     in this case, I will be using 2, and setting the weights to distance
#     """
#
#     print kn_score, metrics.f1_score(labels_test, pred_kn), metrics.precision_score(labels_test, pred_kn), metrics.recall_score(labels_test, pred_kn)

"""
# KN neighbors is best with n_neighbors = 1 or 2.
# accuracy_score = 0.857
# f1 score = 0.4
# precision_score = 0.5
# recall_score = 0.33
"""

"""
SVC
"""

## This loop find the best value for the C parameter and prints the scores.

# c_range = [1,10,25,50,100,500,1000]
# for i in c_range:
#     clf = SVC(kernel='rbf', C = i)
#     clf.fit(features_train, labels_train)
#     pred_svc = clf.predict(features_test)
#     svc_score = metrics.accuracy_score(labels_test, pred_svc)
#
#     print svc_score, metrics.precision_score(labels_test, pred_svc), metrics.recall_score(labels_test, pred_svc)


"""
The value for C did not matter.
# accuracy_score = 0.860
# f1 score = 0
# precision_score = 0
# recall_score = 0
"""

"""
Decision Tree Regressor + AdaBoostRegressor
"""
## Just like the other classifiers, I created a loop to find the best scores
## the codes below have already been set to optmize accuracy (and other scores)

# tree1 = DecisionTreeRegressor(random_state=97)
# treeboost =  AdaBoostRegressor(DecisionTreeRegressor(),random_state = 99)
#
# tree1.fit(features_train, labels_train)
# treeboost.fit(features_train, labels_train)
#
# t1_pred = tree1.predict(features_test)
# tboost = treeboost.predict(features_test)
#
# print "DecisionTreeRegressor Score"
# print metrics.accuracy_score(labels_test, t1_pred)
# print metrics.f1_score(labels_test, t1_pred)
# print metrics.precision_score(labels_test, t1_pred)
# print metrics.recall_score(labels_test, t1_pred)
# print "-"
# print "AdaBoostRegressor Score"
# print metrics.accuracy_score(labels_test, tboost)
# print metrics.f1_score(labels_test, tboost)
# print metrics.precision_score(labels_test, tboost)
# print metrics.recall_score(labels_test, tboost)

"""
Decision Tree Regressor + AdaBoostRegressor Scores (both were the same)
accuracy_score = 0.880952380952
f1_score = 0.545454545455
precision_score = 0.6
recall_score = 0.5
"""



"""
DecisionTreeClassifier - The classifier I chose.
"""

## For loops have been used to find the best parameters

# clf = DecisionTreeClassifier(criterion='entropy',  random_state = 164)
# clf.fit(features_train, labels_train)
# pred_tree = clf.predict(features_test)
# tree_score = metrics.accuracy_score(labels_test, pred_tree)

clf = KNeighborsClassifier(n_neighbors=3, weights='uniform')
clf.fit(features_train, labels_train)
pred_kn = clf.predict(features_test)
kn_score = metrics.accuracy_score(labels_test, pred_kn)

# print kn_score, metrics.f1_score(labels_test, pred_kn), metrics.precision_score(labels_test, pred_kn), metrics.recall_score(labels_test, pred_kn)

# print len(labels_test)
# count = []
# for k,i in enumerate(labels_test):
#     if i == 1:
#         count.append(k)
#
# print count
#
# count2 = []
# for k,i in enumerate(pred_tree):
#     if i == 1:
#         count2.append(k)
#
# print count2

# print tree_score
# print metrics.f1_score(labels_test, pred_tree)
# print metrics.precision_score(labels_test, pred_tree)
# print metrics.recall_score(labels_test, pred_tree)

"""
DecisionTreeClassifier Score
accuracy_score = 0.880952380952
f1_score = 0.615384615385
precision_score = 0.571428571429
recall_score = 0.666666666667
"""
pca = decomposition.PCA()


"""
# Task 6: Dump your classifier, dataset, and features_list so anyone can
# check your results. You do not need to change anything below, but make sure
# that the version of poi_id.py that you submit can be run on its own and
# generates the necessary .pkl files for validating your results.

"""

dump_classifier_and_data(clf, my_dataset, features_list)
