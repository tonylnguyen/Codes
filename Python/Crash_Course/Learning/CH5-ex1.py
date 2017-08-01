#using if statements with lists
cars_brand = ['accord','bmw','acura']
for car in cars_brand:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#if you want to check the condtion us == and not =
#to do a case check

car = 'Audi'
print(car == 'audi') #false
print(car.lower() == 'audi') #true

# != means does NOT equal too

if cars_brand !== 'lexus':
    print("I don't own a Lexus.")

#checking if the value is in the lists

print('accord' in cars_brand) #true

#checking to see if item is in the list
#remember we defined car as "Audi" ealier
if car not in cars_brand:
    print("This car is not in your list.")
