#!/usr/bin/python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import pickle
import re
import sys
from nltk.corpus import stopwords
sys.path.append( "/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_5/ud120-projects/tools" )
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_5/ud120-projects/text_learning/from_sara.txt", "r")
from_chris = open("/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_5/ud120-projects/text_learning/from_chris.txt", "r")

# sara = parseOutText(from_sara)
# chris = parseOutText(from_chris)


# for i in remove_words:
#     if i in chris:
#         chris = chris.replace(i, '')
#     if i in sara:
#         sara = sara.replace(i, '')
#
# chris = chris.split(' ')
# sara = sara.split(' ')


from_data = []
word_data = []

# for words in chris:
#     word_data.append(words)
# for words in sara:
#     word_data.append(words)
#
# from_data.append(sara)
# from_data.append(chris)
### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        # temp_counter += 1
        if temp_counter < 200:
            path = os.path.join('..', path[:-1])
            email = open(path, "r")
            ### use parseOutText to extract the text from the opened email
            parsed_email  = parseOutText(email)


            ### use str.replace() to remove any instances of the words
            remove_words = ["sara", "shackleton", "chris", "germani", 'sshacklensf','cgermannsf']
            for words in remove_words:
                parsed_email = parsed_email.replace(words, '')


            ### append the text to word_data
            word_data.append(parsed_email)

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            if 'ara' in name:
                from_data.append(0)
            else:
                from_data.append(1)

            email.close()

# print "emails processed"
from_sara.close()
from_chris.close()

#answer for other quiz
print word_data[152]

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )

#answer for other quiz

## in Part 4, do TfIdf vectorization here
stop = stopwords.words('english')
tfidf = TfidfVectorizer(stop_words = 'english')
tfidf.fit_transform(word_data)

print (tfidf.get_feature_names()[34597])

# for words in stop_words
