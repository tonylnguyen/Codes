# storing functions in modules
# storing different codes in other files and keeping your main code clean
# a module is a file ending in .py (basicly all the files you created are
# modules)
# imports should be on top of the code, but for thix ex, it will not be
# allows any functions in CH8_ex8_modules will now be available here
import CH8_ex8_modules
# location_of_function.function_name(parameters)
CH8_ex8_modules.make_pizza(12, 'mushroom', 'cheese')
CH8_ex8_modules.make_pizza(16, 'cheese', 'garlic', 'ham')

# importing with an alias
import CH8_ex8_modules as p
p.make_pizza(16, 'garlic', 'noodles')

# importing functions from a module
from CH8_ex8_modules import make_pizza
make_pizza(24, 'olives', 'meat', 'bacon')

# giving an alias for functions
from CH8_ex8_modules import make_pizza as mp
mp(10, 'cheese')

# importing all functions
from CH8_ex8_modules import *  # the astrisk signifies all
