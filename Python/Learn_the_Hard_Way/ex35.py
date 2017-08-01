from sys import exit

def gold_room(): # if bear_room passes, run gold_room functions
    print "This room is full of gold! How much do you take?"

    choice = raw_input("> ") #asks users for a number

    if "0" in choice or "1" in choice: # if choice has 1 or 0, converts choice into an integer
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.") # otherwise, dead function


    if how_much < 50: # if how muhc is less than 50
        print "Nice, you are not greed, you win!" # we win!
        exit(0) #program ends 
    else:
        dead('You are too greedy. You bastard!') #otherwise, dead

def bear_room(): # if start choses left, triggers the bear_room
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False # sets this variable to False boleon

    while True: # loops through the if statement until false (when gold_room function starts.)
        print "take honey, taunt bear, open door"
        choice = raw_input("> ") # asks users for an input

        if choice == "take honey": # if user takes honey, dead() function starts
             dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved: #while bear_moved is false, you can taunt the bear
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True # if you taunt the bear, bear moved is True
        elif choice == "taunt bear" and bear_moved: # if you taunt the bear again, dead functions starts
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved: # if bear moved and you open door, triggers gold room
            gold_room()
        else:
            print "I got no idea what that means." # any other choice prints This

        # loops through bear_room until gold_room starts

def cthulhu_room(): # if start is right, cthulhu_room rom triggers
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ") # asks users to flee or head

    if "flee" in choice: # if choice = flee run start function
        start()
    elif "head" in choice: # if choice = head run dead function
        dead("Well that was tasty!")
    else:
        cthulhu_room() # if neither, run cthulhu_room


def dead(why): #when ever this triggers, why = string statement (set by other function)
    print why, "Good job!" # prints why parameter, along with Good Job
    exit(0) #exits program

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("left or right? > ") # asks for user's input

    if choice == "left": # if choice is left, bear_room function starts
        bear_room()
    elif choice == "right": # if choice is right, cthulhu_room function starts
        cthulhu_room()
    else: #anything else, dead function starts
        dead("You stumble around the room until you starve.")


start()
