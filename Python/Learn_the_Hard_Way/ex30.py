people = 50
cars = 20
trucks = 5


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

if (trucks > cars): # checks to see if truckts is greater then cars
    print "Having so many trucks is not fuel efficient." # if it is, print this statement
elif people > 40: # if statement above does not pass, check to see if this one does
    print "There is no way we can fit all these peope." # if passed, run this statement
else: # if all statements above did not pass, print the statement below
    print "Everything is A-Okay"


"""
Try to guess what elif and else are doing.
If there are multiple condtions needed, elif (else if) can be used to fulfil the needed requirements.
Important to note that the code will stop running once one of the condtions are met.

Change the numbers of cars, people, and trucks and then trace through each if-statement to see what will be printed.
(done!)

Try some more complex boolean expressions like cars > people or trucks < cars.
Above each line write an English description of what the line does
"""
