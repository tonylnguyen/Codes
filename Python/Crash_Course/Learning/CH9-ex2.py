class Car():

    def __init__(self, year, make, model):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def car_description(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        long_name2 = str(self.year) + " " + \
            self.make.title() + " " + self.model.upper()
        if len(self.model) <= 3:
            return long_name2
        else:
            return long_name.title()

    def read_odometer(self):
        return("This car has " + str(self.odometer) + " miles on it.")

    def update_odometer(self, mileage):
        self.odometer = mileage

    def increment_odometer(self, miles):
        self.odometer += miles

tonys_car = Car(2011, 'acrua', 'tsx')
print(tonys_car.car_description())

tuans_car = Car(2015, 'scion', 'frs')
print(tuans_car.car_description())

johnnys_car = Car(2007, 'kawasaki', 'ninja 300')
print(johnnys_car.car_description())

print(tonys_car.read_odometer())

# we can change the value of odometer in three ways
# change the value in the function
# set value in the method, increment value through method

# changing the value in the fucntion
tonys_car.odometer = 60000
print(tonys_car.read_odometer())

# setting a value through a method by creating a new function see line 20
tuans_car.update_odometer(13000)
print(tuans_car.read_odometer())

# increment through the method see line 23
johnnys_car.update_odometer(16000)
print(johnnys_car.read_odometer())
johnnys_car.increment_odometer(500)
print(johnnys_car.read_odometer())

print('-' * 10)
# exercises


class Restaurant():

    def __init__(self, name, food):
        self.name = name
        self.food = food
        self.serve = 0

    def describe_restaurant(self):
        print("This restaurant is called " + self.name.title() + ".")
        print("It serves " + self.food.title() + " food.")

    def open_close(self):
        print(self.name.title() + " is open.")

    def daily_served(self):
        print(self.name.title() + " served " + str(self.serve) + ' people.')

    def update_served(self, eating):
        self.serve = eating

    def adjust_serve(self, adjust):
        self.serve += adjust

gochi = Restaurant('gochi', 'japanese')
gochi.daily_served()

gochi.update_served(50)
gochi.daily_served()

gochi.adjust_serve(25)
gochi.daily_served()

print('-' * 10)


class Users():

    def __init__(self, user_name, user_first, user_last):
        self.user_name = user_name
        self.user_first = user_first
        self.user_last = user_last
        self.failed_login_attempts = 0

    def user_info(self):
        print(self.user_first + ' ' + self.user_last + " : " + self.user_name)

    def bio(self):
        print("Hello my name is " + self.user_first.title() + ".")

    def failed_attempt(self, failed):
        self.failed_login_attempts += failed
        print("Failed attempt #" + str(self.failed_login_attempts) + '.')
        print("Please try again.")

    def reset_attempt(self):
        self.failed_login_attempts = 0


tony = Users('xpfighter', 'tony', 'nguyen')
tony.failed_attempt(1)
tony.failed_attempt(1)
tony.reset_attempt()
print(tony.failed_login_attempts)
