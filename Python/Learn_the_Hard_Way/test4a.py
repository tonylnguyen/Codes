# Write a function that maps a list of words into a list of integers representing
# the lengths of the corresponding words. Your function should have one input
# parameter (list of words), and return a dictionary containing each
# word->length.
import sys

list1 = "fjdskla fjdalk fjdsaklghwag;haw;"


def word_len(words):
    dicter = {}

    if type(words) == type(1):
        print "We need a string, not an integer"
        sys.exit()

    if type(words) == type([]):
        for i in words:
            dicter[i] = len(i)
    else:
        splitter = words.split(' ')
        for i in splitter:
            dicter[i] = len(i)
    return dicter

print word_len(list1)
