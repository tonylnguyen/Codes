print "You enter a dark room with two doors. Do you go through door #1 or #2?"

door = raw_input("1 or 2? > ")

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input('1 or 2? > ')

    if bear == '1':
        print "The bear eats your face off. You died."
    elif bear == '2':
        print "the bear eats your legs off. You are paralyzed!"
    else:
        print  "Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("1, 2, or 3? > ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

else:
    print "Oh, you thought by not playing this game, you would live?"

if door != "1" or "2":
    print "Well, lets play another game."
    print "It's time to check into the hotel California."
    print "Which room would you like to stay in?"

    room = raw_input("37 or 64? > ")

    if room == "64":
        print "You can check out any time you like, but you can never leave!"
    elif room == "37":
        print "This could be heaven or this could be Hell."
    else:
        print "It's a really good song!"
