# objects and classes
class Dog():
    # make/define a class called dog (classes start with a Capital letter!)
    # A function that is part of a class also acts as a method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " just rolled over.")

# to access the class we need an object
my_dog = Dog('snoopy', 13)
# ^ this creates the my_dog object and tells python it belongs to the Dog class
print("My dog is " + my_dog.name.title())

my_dog.sit()  # this is out you call functions in the class
my_dog.roll_over()

your_dog = Dog('koopa', 4)
your_dog.sit()
your_dog.roll_over()
print('-' * 20)
# exercises


class Restaurant():

    def __init__(self, name, food):
        self.name = name
        self.food = food

    def describe_restaurant(self):
        print("This restaurant is called " + self.name.title() + ".")
        print("It serves " + self.food.title() + " food.")

    def open_close(self):
        print(self.name.title() + " is open.")

gochi = Restaurant('gochi', 'japanese')
print(gochi.name.title())
gochi.describe_restaurant()

afk = Restaurant('afk lounge', 'american')
afk.open_close()
print('-' * 20)


class Users():

    def __init__(self, user_name, user_first, user_last):
        self.user_name = user_name
        self.user_first = user_first
        self.user_last = user_last

    def user_info(self):
        print(self.user_first + ' ' + self.user_last + " : " + self.user_name)

    def bio(self):
        print("hello my name is " + self.user_first)

tony = Users('xpfighter', 'tony', 'nguyen')

print(tony.user_name)
print(tony.user_info())
# notice if we try to print a function it will also give us 'none'
tony.bio()
# ^ remember to print functions like this
print('-' * 20)
