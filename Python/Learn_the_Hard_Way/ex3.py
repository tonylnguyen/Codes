from __future__ import division
# ^ forces python to convert intergers to floats for the entire exercise
# if I wanted one instances of a float, I would use float(x)

# + plus - add
# - minus =subtract
# * astrisk - muliplies
# / forward slash - divideds
# % Mundo - divideds two intergers and returns the remainder
# < less than
# > greater than
# >= greater or equal
# <= less than or equal

print('I will now count my chickens:')
#prints the string, I will now count my chickens:

print('Hens:'), 25 + 30 / 6
#prints Hens: 25 + (30 / 6)

print('Roosters:'), 100 - 25 * 3 % 4
#prints roosters 100 - ((25 * 3) % 4)

print("Now I will count the eggs:")
#prints Now I will count the eggs:

print (3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
# 3 + 2 + 1 - 5 + (4 % 2) - (1 / 4) + 6
# 3 + 2 + 1 - 5 + (0) - (0) + 6
# 5 + 1 - 5 + (0) - (0) + 6
# 6 - 5 + (0) - (0) + 6
# 1 + (0) - (0) + 6
# 1 - (0) + 6
# 1 + 6
# 7 or 6.75 if using float

print ('\nIs it true that 3+2 < 5 -7')
print (3+2 < 5 -7)
# ((3+2) < (5 - 7))
# (5 < -2)
# is 5 less than 2? returns False

print('\n')
print ("What is 3 + 2?", 3 + 2)
# prints 5
print ("What is 5 - 7?", 5 - 7)
# prints -2

print ("\nOh, that's why it's False.")

print ("\nHow about some more.")

print ("Is it greater?", 5 > -2)
# prints out True
print ("Is it greater or equal?", 5 >= -2)
# prints True
print ("Is it less or equal?", 5 <= -2)
# prints False
