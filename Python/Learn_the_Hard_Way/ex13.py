from sys import argv


script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
fourth = raw_input("Is this right? ")

print "Let's see if I am understanding this. %r is first, %r is second, %r is third, %r is fourth." % (first, second, third, fourth)

# when 2 or less (or 4 or more) arugments are given python doesn't know
# what to place for the arguments
