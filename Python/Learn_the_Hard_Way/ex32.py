#  Creating a list with values in it
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print "This is count %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit

for i in change:
    print "I got %r" % i

elements = []

for i in range(0, 6):
    print "adding %d to the list." % i
    elements.append(i)

for i in elements:
    print "Elements was: %d" % i

# range() is a method that creates a list of numbers, with the first
# parameter being the starting point and the last parameter being the last
# (-1)

# This is how to avoid a for-loop using ranges
elements = range(0,9)
print elements

print help(list)
