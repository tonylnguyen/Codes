requested_topping = ['cheese','mushroom','garlic','bell pepper']

for toppings in requested_topping:
    print('Adding '+ toppings + " to your pizza.")
print("\n")

for toppings in requested_topping:
    if toppings == 'bell pepper':
        print(toppings + " is not available.")
    else:
        print(toppings + " is now on your pizza.")

print("\n")

#checking to see if the list is empty
requested_topping = []

if requested_topping:
    for toppings in requested_topping:
        print(toppings+ " is now in your pizza")
    print("Done!")
else:
    print("Here is a plain pizza.")

print("\n")

#checking for none avaible items
available_toppings = ['cheese','mushroom','garlic','bell pepper']
requested_topping = ['cheese','wine','garlic']

for toppings in requested_topping:
    if toppings in available_toppings:
        print(toppings + " has been added.")
    else:
        print(toppings + " is not avaible.")
print("\n")

#exercises

users = ['admin','sam','joanne','tony']

for user in users:
    if user == 'admin':
        print("Welcome " + user.title() + " the website is yours to command.")
    else:
        print("Welcome back " + user.title() + ".")

users1 = []

if users1:
    for user in users1:
        print("Hello " + user.title)
else:
    print("Please add some users.")

current_users = users[:]
new_users = ['sam','julie','jen','tony']

for new_user in new_users:
    if new_user in current_users:
        print('The user ' + new_user.title() + " has already been added.")
    else:
        print(new_user.title() + " has been added.")
        current_users.append(new_user) #appending the new users to current user.

print(current_users)

numbers = range(1,10)

for number in numbers:
    if number == 1:
        print(str(number)+"st")
    elif number == 2:
        print(str(number)+"nd")
    elif number == 3:
        print(str(number)+'rd')
    else:
        print(str(number)+'th')
