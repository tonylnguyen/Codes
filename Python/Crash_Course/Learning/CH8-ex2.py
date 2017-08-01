#Passing arguments

#positional arguments where python takes the argument based on the position

def animals (animal_type,animal_name):
    print("I have a " + animal_type + " and it's name is " + animal_name.title() + '.')

animals('dog','snoopy') #this is a positional arguement where dog and snoopy are set to the position of the parameters
animals('fido','cat') #notice how errors can be made by putting arguements in wrong positions
#to prevent this we can use a keyword argument where we define the values of the parameters

animals(animal_type = 'dog', animal_name = 'koopa')
#if we give a keyword argument there will be less mistakes
#default values

def work_place (name, work = 'kotetsu'): #the position of the default value matters (must be last)
    print(name + " works at " + work)

#different ways to call the functions
work_place(name = 'tony')
work_place('sally')
work_place(name = 'joe', work = 'peets')
work_place('niko','gyu')

#exercises

def make_shirts(size = 'large'):
    print("You have ordered a shirt in size " + size)

make_shirts()

def describe_city(city = 'San Jose', country = 'USA'):
    print("I live in " + city.title() + ' which is in ' + country)

describe_city()
describe_city('SANATA CLARA', 'Mexico')
