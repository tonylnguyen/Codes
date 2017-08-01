

def game(number):
    game_board = """
    -----------------
    |   |   |   |   |
    |   |   |   |   |
    |   |   |   |   |
    """
    end = """----------------- """
    if type(input) == type(""):
        print "We need an integer not a string."
    else:
        print (game_board * number) + end

game(5)
