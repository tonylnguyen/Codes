file_name = '/Users/tonynguyen/Desktop/Codes/Python/Crash_Course/Learning/Ch10_empty.txt'

with open(file_name, 'w') as blank:
    blank.write('Writing in a blank file.')
    blank.write('This is how you write 2 lines')
    blank.write('\nRemember to use breakers to space lines')

# 'w' tells python we want to open the file in write mode
# 'r' = read
# 'a' = append (allows you to write files without deleting old info)
# 'r+' = read and write
# python can only write in strings. if numbers are used be sure to use str()

with open(file_name, 'a') as add_on:
    add_on.write("\n\nI am appending new lines to the file")
