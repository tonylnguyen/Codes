# Write a program that secretly selects a number between 1 and 100, and repeatedly
#  asks the user to guess it until the guess is correct. If the guess is incorrect
#  and lower than the secret number, the program should print "too low". If the
#  guess is incorrect and higher than the secret number, the program should print
#  "too high".

import random



def high_low():
    ran_number = random.randint(1,100)
    while True:
        user_number = int(raw_input('Pick a number 1-100.\n> '))
        if user_number == ran_number:
            print("You got it right!!!")
            break
        if ran_number > user_number:
            print("Too low.")
        if ran_number < user_number:
            print ("Too high.")



high_low()
