"""  bag of words vectorizor """
from sklearn.feature_extraction.text import CountVectorizer as cv

string1 = 'Hey Brian, go get me sone water best, Tony'
string2 = 'Dearest Tony, go suck a cock. Bye, Brian'
string3 = 'Morning Brian, you little bitch, I am gonna report you. From, Tony'

#you need to put the emails in a list to vectorize them
emails = [string1, string2, string3]

#assigns the classifier
vectorize = cv()

#fits the data and transform (similar to predict) the emails
bag_of_words = vectorize.fit(emails)
bag_of_words = vectorize.transform(emails)

print bag_of_words
"""
How to read bag of words

(2,20)  2
(string3, word number 20)  #numer of occurance

"""

# this prints what feature number a word is 
print vectorize.vocabulary_.get('you')



""" Stems/Roots of words """

from nltk.stem.snowball import SnowballStemmer as snowball
stemmer = snowball('english')

#this prints the stem/root of a word
# print stemmer.stem('unresponsive')


#TFIDF Representation

# TF - term frequency (how often it occurs)
# IDF - inverse doc frequency (how often the word occurs in the entire body)
