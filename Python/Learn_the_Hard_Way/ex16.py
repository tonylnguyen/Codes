from sys import argv

script, filename = argv
# python ex16.py ex16.txt
# this is the code i used in the interpreter

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C.")
print("If you do want that, hit RETURN.")

raw_input("?")

print ("Opening the file...")
target = open(filename, 'w')
# the parameter w stands for write which allows us to
# alter the file

# It is not necessary to truncate the txt file because
# the w mode will overwrite the file.

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print("I'm going to write these lines to the file now.")

target.write(line1 + '\n' + line2 + '\n' +  line3)

print("Saving file.")
target.close()

print("\nHere is your new file.")
target = open(filename)
print(target.read())
