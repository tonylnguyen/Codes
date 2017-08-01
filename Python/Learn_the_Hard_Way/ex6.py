
# Creates the variable x and sets the value of x to a string. Also x has
# two formatters in it
x = 'There are %d types of people.' % 10
# Creates the variable binary and sets the value to 'binary'
binary = 'binary'
# Creates the variable do_not and sets the value to don't
do_not = "don't" # 1) string in string
# Creates the variable y and sets the value of x to a string. Also x has
# two formatters in it
y = "Those who know %s and those who %s." % (binary, do_not)

# prints variables x and y (both strings with formatters)
print x
print y

# prints out a string with the formatters x and y
print "I said: %r." % x # 2) string in string
print "I also said: '%s'." % y # 3) string in string

# creates a variable called hilarious and sets the value to False
hilarious = False
# creates a string with a formatter
joke_evaluation = "Isn't that joke so funny?! %r" # 4) string in string
# prints the variable joke_evaluation and sets the formatter to hilarious
print joke_evaluation % hilarious

# creates a string
w = "This is the left side of..."
e = "a string with a right side."
# adds two strings together and prints it out
print w + e
# extra: Strings and intergers cannot be printed (concatenation error)
# together unless the str() or int () methods are used
