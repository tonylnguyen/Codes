#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
# this file is so CH9-ex4 can use to import classes
# The class below has been copied from CH9-ex3


class Cars():

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def car_description(self):
        print(str(self.year)+' '+self.make.title() + ' ' + self.model.title())

    def ride_wheels(self):
        if len(self.model) == 3:
            print("The " + self.model.upper() + " has 4 wheels.")
        else:
            print("The " + self.model.title() + " has 4 wheels.")


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
