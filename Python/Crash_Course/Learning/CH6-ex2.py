#Looping through dictionaries
user0 = {'username':'admin','first_name':'tony','last_name':'nguyen'}
user1 = {'username':'Sam1990','first_name':'sam','last_name':'lin'}
user2 = {'username':'swishers','first_name':'niko','last_name':'nobida'}

user_names = {'tony':'AdmiN','sam':'Sam1990','jen':'jenNERvu','tuan':'beefcake'}

jobs = {'jen':'kitties','tony':'nothing','tuan':'taste'}

for key, value in user0.items():
    print('\nKey: ' + key.title())
    print('Value: ' + value.title())

#.items() returns a list of key-value pairs
#notice how it is NOT printed in the order stored.
#this loops through ALL the key-value pairs in the dictionary

print('---'*10)

#loopting through only KEYS or VALUES in a dictionary
for keys in user2.keys():
    print(keys.title())
print('\n')
for values in user1.values():
    print(values.title())
print('---'*10)

#------
user_queue = ['tony','sam']

for names in user_names:
    print(names.title())

    if names in user_queue:
        print("  Hey " + names.title() + " your username is " + user_names[names].title() )
        #im not sure why using names prints the key and the value in the if statement
print('---'*10)

#looping through a stored dictionaries using the .sort() method

for names in sorted(user_names.keys()):
    print('Hello ' + names.title() + ' your username is ' + user_names[names])

print('---'*10)

#When looping through the values of a dictionary use the .values() method

#excercises

country_river = {'usa':'mississippi','egypt':'nile','panama':'panama cannel'}

for country in country_river.keys():
    print('The country ' + country.title() + ' has the river ' + country_river[country].title() + ' flowing in it.')

for country, river in country_river.items():
    print("\nCountry: " + country)
    print("River: " + river)

print'Values: %r' % country_river.items()
