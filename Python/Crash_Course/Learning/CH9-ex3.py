#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
# having issues with python versions (2 and 3)
# line 1 (called shebang) tells atom for this project, just python 3

# child class - taking info from the parent class for your code


class Cars():

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def car_description(self):
        print(str(self.year)+' '+self.make.title() + ' ' + self.model.title())

    def ride_wheels(self):
        print("The " + self.model.title() + " has 4 wheels.")


tonys_car = Cars(2011, 'acura', 'tsx')
tonys_car.car_description()


class Motorcycle(Cars):  # we put the class Car in the parameter
    """ Represents an aspect of car, mainly motorcycles/scooters """

    def __init__(self, year, make, model):
        """ initialize attributes of the parent class. """
        super().__init__(year, make, model)

    def motorcycle_class(self, type1):
        self.type = type1
        print(self.make.title() + " " + self.model.title() +
              ' is a ' + self.type + ' bike.')
    # now motorcycles has it's own instance seperate from the Car class

    def ride_wheels(self):
        print("Motorcycles only has 2 wheels.")


johnnys_car = Motorcycle(2007, 'kawasaki', 'ninja 250')
johnnys_car.car_description()
johnnys_car.motorcycle_class('sports')

# how to override parent class' functions see line 18 vs 39
tonys_car.ride_wheels()
johnnys_car.ride_wheels()

# exercises


class Restaurant():

    def __init__(self, name, food):
        self.name = name
        self.food = food

    def describe_restaurant(self):
        print("This restaurant is called " + self.name.title() + ".")
        print("It serves " + self.food.title() + " food.")

print('-'*20)


class Kiosk(Restaurant):

    def __init__(self, name, food):
        super().__init__(name, food)
        self.flavors = ['chocolate', 'strawberry', 'vanilla']
        # bonus points for using a list!

    def flavor_list(self):
        print("These are the flavors " + self.name.title() + ' has.')
        for flavor in self.flavors:
            print(flavor.title())

tin_pot = Kiosk('tin pot', 'ice cream')
tin_pot.flavor_list()
print('-'*20)


class Users():
    """ basic user info """
    def __init__(self, username, user_first, user_last):
        self.username = username
        self.user_last = user_last
        self.user_first = user_first

    def user_bio(self):
        print("Username: " + self.username)
        print(self.user_first.title() + ' ' + self.user_last.title())


class Admin(Users):
    """ Admins and their power """
    def __init__(self, username, user_first, user_last):
        super().__init__(username, user_first, user_last)
        self.admin_power = ['delete posts', 'ban users', 'manages page']
        self.privileges = Privileges()


class Privileges():

    def __init__(self, user=False):
        self.user = user
        self.admin_power = ['delete posts', 'ban users', 'manages page']


    def show_privileges(self = True):
        if self.user is False:
            print("You can only post messages")
        else:
            print("These are the power of the Admin:")
            for power in self.admin_power:
                print(power)


tony_xpfighter = Users('admin', 'tony', 'nguyen')
tony_xpfighter.user_bio()


print('-'*20)
sam_admin = Admin('admin', 'sam', 'lin')
sam_admin.privileges.show_privileges()
