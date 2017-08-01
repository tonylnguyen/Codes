def add(a, b):
    print("Adding %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print("Subtracting %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("multipling %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print('Divide %d / %d' % (a, b))
    return a / b

print(" Let's do some math with just functions.")

age = add(20,7)
height = subtract(68,4)
weight = multiply(65,2)
iq = divide(200,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# a puzzle for me!

print("Here is a puzzle.")

what = add(age, subtract(height, (multiply(weight, divide(iq,2)))))
print "That becomes: ", what, "Can you do it by hand?"

# if done by hand
print (27+ (64 - (130 * (100 / 2))))

print (age*height)/2


# returns is simular to print, but instead of priting a statement
# it ruturns a value (which can later be used with other variables and functions)
