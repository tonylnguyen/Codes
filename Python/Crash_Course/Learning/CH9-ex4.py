#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
# we have created a file called CH9_import so we can import files over

from CH9_import import Cars, Motorcycle
# you can import multiple classes like so ^^^
# to import an entire module, it is simply, import CH9_import

# states the import the class Cars from the CH9_import file
# imporint files allows for more cleaner code files
tonys_car = Cars(2011, 'acura', 'tsx')
tonys_car.car_description()
tonys_car.ride_wheels()

johnnys_bike = Motorcycle(2007, 'kawasaki', 'ninja 250')
johnnys_bike.motorcycle_class('sports')
johnnys_bike.ride_wheels()
