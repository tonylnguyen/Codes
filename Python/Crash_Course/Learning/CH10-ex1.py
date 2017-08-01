# ch10 is about working with files and expections
# when python reads text files, it reads it as a string
file_path = '/Users/tonynguyen/Desktop/Codes/Python/Crash_Course/Learning/CH10_txt.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

# with statements tells python to open then close the file when you are done

# with open('CH10_txt.txt') as file_object:
#    file_object.write("I'm the first line of the file!\n")
#    contents = file_object.read()
#    print(contents)

# the code at line 8 is supposed to work but idk why it doesn't
# it keeps saying it can't find the file path, use code @ line 3 instead
print("-" * 20)

with open(file_path) as read_lines:
    for lines in read_lines:
        print(lines)
# this is how you print lines by lines
print("-" * 20)

# if we want to remove the blank lines space we use rstrip
with open(file_path) as strip:
    for lines in strip:
        print(lines.rstrip())
print("-" * 20)

# making a list of lines from a file after the
# with statement (when the file is already closed)
with open(file_path) as make_more:
    lines = make_more.readlines()

for line in lines:
    print(line.rstrip())
print("-" * 20)

# working with the conents of a file (using codes from line 37-41)
empty = ''
for line in lines:
    empty += line.rstrip()
# the code above prints the file in one line

print(empty)
print(len(empty))
print('-'*20)
# use int() or float() if you want to use txt as an interger

with open(file_path) as slice_path:
    open_file = slice_path.read()
    print(open_file[:4])
print('-'*20)

pi_number = '/Users/tonynguyen/Desktop/Codes/Python/Crash_Course/Learning/CH10_txt.txt'

with open(pi_number) as b_day:
    is_in = b_day.read()

#my_birthday = input('When is your birthday (mmddyy)?')
#if my_birthday in pi_number:
#    print('your birthday is in the first 200 pi numbers')
#else:
#    print('IDK')

# exercises

things_learned = '/Users/tonynguyen/Desktop/Codes/Python/Crash_Course/Learning/CH10_practice.txt'

with open(things_learned) as learned:
    copy = learned.read()
    print(copy)
