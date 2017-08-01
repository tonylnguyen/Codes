#functions
#structure: def name_of_fucntion ()
#               does something

def greet_user(): #creating/naming the function
    """ Display a greeting""" #describing what the function does (not) necessary
    print('Hello') #

greet_user()

def hello_user(username): #an example for something that goes into the ()
    print("Hello " + username.title())

hello_user('tony')

def favorite_book(book_name): # def function_name (parameter)
    print("My favorite book is " + book_name.title())

favorite_book('alice in wonderland') #alice in wonderland is the arguments
