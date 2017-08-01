cars = 100
# creates a variable named "cars" and sets the value to cars to 100
space_in_a_car = 4.0
# creates a variable called space_in_a_car and sets value to a float 4.0
drivers = 30
# creates a variable called drivers and sets the value to 30
passengers = 90
# creates a variable called passengers and sets the value to 90
cars_not_driven = cars - drivers
# creates a vraible called cars_not_driven.
# sets the value to cars - drivers (100-30)
# aka sets value to 70
cars_driven = drivers
# creates a variable called cars_driven and sets value to drivers (30)
carpool_capacity = cars_driven * space_in_a_car
# creates variable called carpool_capacity
# sets value to cars_driven * space_in_a_car (30 * 4)
# aka sets value to 120
average_passengers_per_car = passengers / cars_driven
# creates a variable called average_passengers_per_car
# sets value to passengers/cars_driven (90/30)
# aka sets value to 3

# prints out the strings in quotes, and the value of the variable used
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


# Traceback (most recent call last):
#  File "ex4.py", line 8, in <module>
#    average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined

# This error that Zed recieved is due to the python calling the variable
# 'average_passengers_per_car', but the value for car_pool_capacity was
# not set. Since car_pool_capacity did not have a value, python did not
# know what to do when average_passengers_per_car (which contains
# car_pool_capacity) was called.


# Study Drills

#I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
#   Depending on the purpose of the code, it could be necessary. Some cars have half seats (eg: for children). Using a floats can make it easier.
#   If a float is not used, python (when doing math) would round our queries which may not result in the expected outcome.

#Remember that 4.0 is a floating point number. It's just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point.
#Write comments above each of the variable assignments.
#Make sure you know what = is called (equals) and that it's making names for things.
#Remember that _ is an underscore character.
#Try running python from the Terminal as a calculator like you did before and use variable names to do your calculations. Popular variable names are also i, x, and j.

x = 5
i  = 10
j = x%i #(5)

print(j)
