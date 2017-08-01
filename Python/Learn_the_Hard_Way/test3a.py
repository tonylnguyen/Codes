def test(): # creates the function
    master_list = [] # creates and list to store the dictonary key/value
    multiplier = 1 # sets value for our multiplier
    while multiplier < 13: # starts a while loop, ends at 12
        numbers = range(1,13) # creates a list with the range of 1-12
        answers = [] # creates an empty list
        dicto = { multiplier : answers } # creats dictionary, sets key to multiplier and values to answers list
        for i in numbers: # starts a loop on numbers
            answers.append(i*multiplier) # muliplies i and muliplier and appends it to the answers list
        master_list.append(dicto) # appends the dictionary to the master_list
        multiplier = multiplier +1 # increases the value of multiplier +1

    return master_list 

print test()
