#while loops will keep running as long as the code is true
#becareful, if the code is always true, your code will crash!!!!
current_number = 0

while current_number <=5: #sets the condtion, while the number is less than 5...
    print(current_number) #print current_number
    current_number = 1 + current_number #this squences current_number's value by 1
    # line 7 code can be written as current_number += 1

prompt = '\nTell me something, and I will repeat it.'
prompt += "\nEnter 'quit' if you want to end the program.\n >"

message = ' ' #this stores the user's input

while message != 'quit':
    message = input(prompt)
    print(message)
    if message == 'quit': #this is how you can use an if statemenet in a while loop
        print("The progam has been terminated.")
print('-'*20)

#flags are signals to the progam, stating if one more multple events occur, end the program

active = True

while active:
    message = input(prompt).lower() #.lower() we we do not have to worry about casing

    if message == 'quit':
        active = False
        print("The progam has been terminated.")
    else:
        print(message)
print('-'*20)

#a break ends the progam without running the rest of the code

prompt1 = "\nWhich cities have you been to?"
prompt1 += "\nType 'quit' to end the program. \n >"

while True: #this will make the while loop true until it reaches a break statement
    cities = input(prompt1)

    if cities == 'quit':
        break
    else:
        print('Cool I hope ' + cities.title() + ' was a nice place.')
print('-'*20)

#using continue to contunie a loop.

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
print('-'*20)
#excercises

prompt2 = 'Please let me know what kind of toppings to add.'
prompt2 += '\nType quit when you are done. \n >'
pizza_toppings = ' '

pizza_on = True
while pizza_on:
    pizza_toppings = input(prompt2)
    if pizza_toppings == 'quit':
        print('Done!')
        pizza_on = False
    else:
        print('Adding ' + pizza_toppings + ' to your pizza.')

print('-'*20)

age = input("How old are you? \n\t>")
age = int(age)

if age < 3:
    print("Tickets for children under the ages of 3 is free.")
elif age <= 12:
    print("Your ticket will cost $10.")
else:
    print("That will be $15 dollars.")

print('-'*20)
