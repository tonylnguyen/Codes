import sys
import os

print os.getcwd()
os.chdir('/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_5/ud120-projects/validation')
print os.getcwd()

sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
