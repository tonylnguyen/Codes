# this creates a function with 2 parameters and 4 print statements
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print ("You have %d cheeses." % cheese_count)
    print ("You have %d boxes of crackers." % boxes_of_crackers)
    print ("Man that's enough for a party.")
    print ("Get a blanket.\n")

# prints a statement and gives value to the parameters
print ("We can give the functions directly.")
cheese_and_crackers(5,10)

# creates 2 variables (with values) and assigns them to the fucntion parameters
print ("OR, we can can use variables from our scripts:")
amount_of_cheese = 10
amount_of_crackers = 50
# calls the function w/ the variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# calls the function w/ variables and adds integers to the variables
print ("We can even do math inside too:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 10)

#####################
# my function x6   #
#####################

# a kids song
def apples_and_bananas(vowel1):
    print ("I like to %sat %sat %sat, %spples and b%sn%sn%ss" % (vowel1,vowel1,vowel1,vowel1,vowel1,vowel1,vowel1))

apples_and_bananas('a')
apples_and_bananas('e')
apples_and_bananas('i')
apples_and_bananas('o')
apples_and_bananas('u')
apples_and_bananas('y')

# ran out of vowls =(
