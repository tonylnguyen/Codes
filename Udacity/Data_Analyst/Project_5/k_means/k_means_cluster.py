#!/usr/bin/python

"""
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_5/ud120-projects/tools")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_5/ud120-projects/final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it!
data_dict.pop("TOTAL", 0)


### the input features we want to use
### can be any key in the person-level dictionary (salary, director_fees, etc.)
### note: feature_3 needs to be added when necessary
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = 'total_payments'
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


print poi
#this is how kmeans work
kmeans = KMeans(n_clusters=2).fit(finance_features)
pred = kmeans.predict(finance_features)
# Draw(pred, finance_features, poi)

#this is how scalers work
mms = MinMaxScaler(feature_range=(0, 1))
mms_train = mms.fit_transform(finance_features)
mms_test = np.array([200000., 1000000.]) #test the values after its scaled

print mms.transform(mms_test)

### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
feat2 = []
for f1, f2 in finance_features:
    plt.scatter( f1, f2 )
    feat2.append(f1)

mini = []
for i in feat2:
    if i != 0:
        mini.append(i)
