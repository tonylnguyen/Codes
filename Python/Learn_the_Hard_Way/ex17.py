# imports are extra data that can help us write our code
# there are many libraries that contains many data that we can import

from sys import argv
from os.path import exists

script, from_file, to_file = argv
# python ex17.py ex16.txt ex17.txt
# this is the code i used in the interpreter

print "Copying from %s to %s" % (from_file, to_file)

# we do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long." % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w+')
out_file.write(indata)



print "Alright, all done."

# we needed to close the out_file, because it saves the data that was copied into it
out_file.close()
in_file.close()



print('\nHere is a copy of your new file.\n')
reader = open(to_file, 'r')
print reader.read()
reader.close()


#This is at short as I could make the code
#with open(from_file, 'rb+') as file_one, open(to_file, 'rb+') as file_two:
#    file_two.write((file_one.read()))
