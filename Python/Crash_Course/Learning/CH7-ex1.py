#inputs
message = input('tell me something and i will print it. > ')
print (message)

#remember the differences between python 2 and 3  2 uses raw_input 3 uses input
prompt = "test etst teajflkasj test"
prompt +="lets see if this works: "   #extending prompts if you need more than one line

number = input(prompt)
print(number)
#remember that python sees user input as a string NOT interger
number = int(number) #this is how you turn a string into an interger
print(number >= 3)

if number > 5:
    print("yes")
else:
    print('no')

print('-'*20)
#exercises

prompt = "What kind of car would you like to drive? > "
car_rental = input(prompt)
print('Let me see if ' + car_rental +' is in stock.')
print('-'*20)
prompt = 'How many people are in your party? >'
patron = input(prompt)
patron = int(patron)

if patron >=4:
    print("I'm sorry, a party the size of " + str(patron) + " will have to wait.")
else:
    print("There is a table for a party of " + str(patron) +'.')
print('-'*20)

by_10 = input('Enter and number and I will tell you if it is mutliple by 10. > ')
by_10 = int(by_10)

results = by_10 % 10
if results == 0:
    print(str(by_10) + 'is a mutliple of 10')
else:
    print(str(by_10) + ' is not a mutliple of 10')
