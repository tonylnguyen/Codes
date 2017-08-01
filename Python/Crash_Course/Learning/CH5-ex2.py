 i# Conditional If/else statments

age = 20
if age >= 21:
    print("You can enter\n")
elif age >= 18:
    print("You can enter the young adults section")
elif age >= 10:
    print("You will have to enter the youth section")
else:
    print("You are not old enough")

# you can have more then one elif statments

print("\n")
# using condtional statements with lists

toppings = ['mushroom', 'cheese', 'meat', 'pine apples']

if 'mushroom' in toppings:
    print("Adding mushrooms")
if 'cheese' in toppings:
    print("Adding cheese")
if 'wine' in toppings:  # because wine is not in toppings, this will not print
    print("Adding wine")
# an elif/else statement would not work because the code wills stop
# running after the frist pass
print("\n")

alien_color = 'blue'
alien_color2 = 'red'
alien_color3 = 'yellow'

if alien_color == 'blue':
    print("You earned 5 points")

if alien_color == 'red':
    print('You got 10 points.')
else:
    print("You've missed")

if alien_color == 'green':
    print("TEST")
elif alien_color3 == 'yellow':
    print("Flower power")
else:
    print("No points")

print("\n")

age = 18

if age >= 21:
    print("You should be responsible enough.")
elif age == 18:
    print("Make good choices. Use protection")
elif age >= 13:
    print("You are a little to young. Please education yourself.")
else:
    print("You are not mature enough.")

print("\n")

shopping_list = ['bananas', 'apples', 'oranges']

if 'food' in shopping_list:
    print("Get some FOOD")
if 'bananas' in shopping_list:
    print("This shit is bananas")
if 'apples' in shopping_list:
    print("Apples VS Apples")
