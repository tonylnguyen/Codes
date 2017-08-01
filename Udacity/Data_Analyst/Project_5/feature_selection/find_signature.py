#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


# The words (features) and authors (labels), already largely processed.
# These files should have been created from the previous (Lesson 10)
# mini-project.
words_file = "/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_5/ud120-projects/your_word_data.pkl"
authors_file = "/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_5/ud120-projects/your_email_authors.pkl"
word_data = pickle.load(open(words_file, "r"))
authors = pickle.load(open(authors_file, "r"))


# test_size is the percentage of events assigned to the test set (the
# remainder go into training)
# feature matrices changed to dense representations for compatibility with
# classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
    word_data, authors, test_size=0.1, random_state=42)

"""
 A classic way to overfit an algorithm is by using lots of features and
 not a lot of training data. You can find the starter code in
 feature_selection/find_signature.py. Get a decision tree up and training
 on the training data, and print out the accuracy. How many training points
 are there, according to the starter code?
"""



from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test = vectorizer.transform(features_test).toarray()


# a classic way to overfit is to use a small number
# of data points and a large number of features;
# train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train = labels_train[:150]

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score as score

tree = DecisionTreeClassifier()
tree.fit(features_train,labels_train)
pred = tree.predict(features_test, labels_test)

score_test = score(labels_test, pred)
print score_test
word_index = []
for n,i in enumerate(tree.feature_importances_):
    if i != 0:
        print n, i
        word_index.append(n)

# this was used to find the most influenctal word,
# it is no longer needed

# print vectorizer.get_feature_names()[33614]
# print vectorizer.get_feature_names()[14343]

# for i in word_index:
#     print vectorizer.get_feature_names()[i]
