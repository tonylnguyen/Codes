#nesting is storing a dictionary inside a dictionary / listing a dictionary

#copied from ch6-ex2
user0 = {'username':'admin','first_name':'tony','last_name':'nguyen'}
user1 = {'username':'Sam1990','first_name':'sam','last_name':'lin'}
user2 = {'username':'swishers','first_name':'niko','last_name':'nobida'}

users = [user0,user1,user2]

for user in users:
    print(user)
print('---'*10)

#how to auto generate a dictionary in a listing

enemy_aliens = [] #first make a blank listing

for alien_number in range(30): #tells how many aliens to create
    alien_green = {'color':'green','value': 5, 'speed':'slow'} #creates the dictionary of green aliens
    enemy_aliens.append(alien_green) #attaches dictionary to the enemy_aliens list

for enemy in enemy_aliens[:5]:#using a for loop to print on seperate lines
    print(enemy) #prints the first 5 enemy_aliens
print('There are ' + str(len(enemy_aliens)) + ' ships.') #measures the length of enemy_aliens
print('---'*10)

#changing the values in a nest
for yellow_alien in enemy_aliens[:3]: #selects only the first 3 aliens
    if yellow_alien['color'] == 'green': #of the first 3 selects only the green aliens
        yellow_alien['color'] = 'yellow' #the rest changes the key-values for the first 3 aliens
        yellow_alien['value'] = 10
        yellow_alien['speed'] = 'medium'

for enemy in enemy_aliens[:5]:
    print(enemy)
print('---'*10)

#using elif statements in a nest

for red_yellow in enemy_aliens[:10]: #selects only the first 10 aliens
    if red_yellow['color'] == 'green': #of the first 10 selects only the green aliens
        red_yellow['color'] = 'yellow' #the rest changes the key-values for the first 10 aliens
        red_yellow['value'] = 10
        red_yellow['speed'] = 'medium'
    elif red_yellow['color'] == 'yellow': #slects current yellow
        red_yellow['color'] = 'red'  #changes the value of current yellows
        red_yellow['value'] = 20
        red_yellow['speed'] = 'fast'

for enemy in enemy_aliens[:10]:
    print(enemy)
print('---'*10)

#nesting a list inside a dictionary

pizza = {
    'crust':'thin',
    'toppings':['mushroom','cheese','ham']
}
print(pizza)
print("You've ordered a " + pizza['crust'] + '-crusted pizza')
for topping in pizza['toppings']:
    print(topping)
#you can nest a list inside a dictionary when you need a key to have more than one value
#dictionary inside a dictionary
print('---'*10)

web_users = {'xpfighter':{'first_name':'tony','last_name':'nguyen'},'swishers':{'first_name':'niko','last_name':'nobida'},'Sam1990':{'first_name':'sam','last_name':'lin'}}
print(web_users['xpfighter'])

for user_name, bio in web_users.items():
    print('\nUsername: ' + user_name)
    print('User IRN: ' + bio['first_name'].title() + ' ' + bio['last_name'].title())
