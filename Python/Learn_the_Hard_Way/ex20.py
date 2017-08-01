# imports argv from the sys library
from sys import argv

# input_file is ex16.txt
script, input_file = argv

# created a function that reads and prints the parameter
def print_all(f):
    print f.read()

# creats a fuction that sets the parameter's position to 0
def rewind(f):
    f.seek(0)

# creates a function that prints txts lines and reads it
def print_a_line(line_count, f):
    print line_count, f.readline()

# creates a variable that opens input_file
current_file = open(input_file)

print ("First let's print the whole file: \n")

# prints current_file contents
print_all(current_file)

print ("Now let's rewind, kind of like a tape.") # who uses vhl any more?

# sets file position to 0
rewind(current_file)

print ("Let's print three lines:")

# creates a variable called current_line and sets value to 1
current_line = 1

# prints out current_line, and contents of that line
print_a_line(current_line, current_file)

# add's one to current_line changing it's value to 2
# prints out line 2 of the file
current_line =+ 1
print_a_line(current_line, current_file)

# add's one to current_line changing it's value to 3
# prints out line 3 of the file
current_line =+ 1
print_a_line(current_line, current_file)

current_file.close()

# =+ takes the current value of the variable, and adds x (in this case 1)
