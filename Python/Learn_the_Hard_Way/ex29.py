people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The word is doomed!"

if people > cats:
    print "Not many cat! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
     print "People are dogs."

if (people == 20) is True:
    print "There are 20 people."


"""
What do you think the if does to the code under it?
If the conditions are met, the if statement will run/call anything under it.

Why does the code under the if need to be indented four spaces?
There needs to be an indent because it tells python that if the condtions are met
then run everything below it. If there is no indents then the code will return an error.

What happens if it isn't indented?
The code will return expected an indented block

Can you put other boolean expressions from Exercise 27 in the if-statement? Try it.
(see line 28)

What happens if you change the initial values for people, cats, and dogs?
It will change the conditions of the if statement.
"""
