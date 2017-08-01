#coping lists

numbers = range(1,11)
print("The first three numbers are ")

for number in numbers[:3]:
    print(number)

print("\nThese are the middle numbers")
for number in numbers[1:9]:
    print(number)

print("\nThese are the last three:")
for number in numbers[7:10]:
    print(number)


pizza_toppings = ['cheese','pepperoni','mushrooms','garlic']
pizza_toppings.append('bell pepers')

your_toppings = pizza_toppings[:]
your_toppings.append('crap')
print(your_toppings)
print(pizza_toppings)
