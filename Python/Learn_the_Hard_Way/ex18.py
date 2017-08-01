
def print_two(*args):
    arg1, arg2 = args
    print ("arg1: %r, arg2: %r" % (arg1, arg2))

print_two('hello','goodbye')

def print_two_again(arg1, arg2):
    print ("arg1: %r, arg2: %r" % (arg1, arg2))

print_two('hello','goodbye')

def print_one(arg1):
    print ("arg1: %r" % arg1)

print_one('Please leave')

def print_none():
    print "I got nothing."

print_none()


print_two("Tony","Nguyen")
print_two_again("Nguyen","Tony")
print_one("ME")
print_none()

def two_var_sum(x,y):
    print x+y

two_var_sum(5,6)
