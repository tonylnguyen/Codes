# imports argv from the sys library
from sys import argv

# asks users for the file name and opens it (through)
script, ex15_sample  = argv
# python ex15.py ex15.txt
# this is the code i used in the interpreter

txt = open(ex15_sample)

# reads and prints out the txt file
print("Here's your file %r:\n" % ex15_sample)
print txt.read()

# asks users to type the file again via raw_input
print("Type the filename again:\n")
file_again = raw_input("> ")

# takes the raw input and opens file_again
txt_again = open(file_again)
print txt_again.read()

# closes the files we opened
txt.close()
txt_again.close()
