print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)


print "Why so sad?"
answer = raw_input()

print "Your answer: " + answer

# Related to escape sequences, try to find out why the last line has
# '6\'2"' with that \' sequence. See how the single-quote needs to be
# escaped because otherwise it would end the string?

# THere is an escape so the the terminal will treat the raw data as
# regular string
