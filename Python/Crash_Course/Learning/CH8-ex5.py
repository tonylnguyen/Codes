#arbitrary arguments, basicly a function with unlimited arguments

def pizza(*toppings):
    print('Adding to the pizza:')
    for topping in toppings:
        print(topping.title())

pizza('cheese','olives')
pizza('cheese','garlic','wine')

#using arbitrary arguments with positional arguments
print("-"*20)
def ice_cream(cup,*toppings):
    print('Adding these to your ' + cup)
    for topping in toppings:
        print(topping)

ice_cream('cone','sprinkles','choclate')
print("-"*20)

#Using arbitrary arguments with keyword arguments (with dictionaries)

def building_profile(first,last,**user_info): # ** is used for keyword arguments
    profile = {} #created a blank dictionary to store the data
    profile['first_name'] = first #creates a key-value pair
    profile['last_name'] = last #creates a key-value pair
    for key, value in user_info.items(): #creates a key-value pair but the ** lets python know that the user
                                         # will enter 'X' amount of key-value pairs
        profile[key] = value
    return profile

user_profile = building_profile('niko','nobida', work = 'kotetsu', city = 'santa clara')
print(user_profile)
print("-"*20)

#exercises

def sandwiches(*content):
    if len(content) == 1:
        print('Adding this now: ')
    else:
        print('Adding these now: ')
    for stuff in content:
        print(stuff)

sandwiches('cheese','mustard','ham')
sandwiches('parsley','sprouts')
sandwiches('ham')

print("-"*20)

def new_user(first, last, **user_info):
    user = {}
    user['first_name'] = first
    user['last_name'] = last
    for key, value in user_info.items():
        user[key] = value #tells python to append this dictionary as user_info
    return user

xpfighter = new_user('tony','nguyen',age = 26, location = 'san jose', work = 'kotetsu')

print("-"*20)

def cars(manufacturer, line, **others):
    sold = {}
    sold['make'] = manufacturer
    sold['model'] = line
    for key, value in others.items():
        sold[key] = value

tony_nguyen = cars('honda','accord', color = 'green')
