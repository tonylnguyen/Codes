
from sys import argv

script, input_file, output_file = argv

from_file = open(input_file, 'r+')
to_file = open(output_file, 'w+')

def linereader(f):
    counter = 1
    for lines in f:
        to_file.write(str(counter) + ' ' + lines)
        counter += 1

linereader(from_file)
