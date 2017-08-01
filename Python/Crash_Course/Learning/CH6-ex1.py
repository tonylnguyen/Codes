#dictionaries, similar to a list but you define values
# dictionary_name = {'key':'value','key':value}, use braces to initiate dictionaries

alien1 = {'color':'blue','value':5}

print(alien1['color'])
print(alien1['value'])

new_point = alien1['value']
print("you just earned " + new_point + "." )

#adding new values/starting from an empty dictionary

alien1['x position'] = 0
alien1['y position'] = 25

print(alien1) #python doesn't care about the order of the values, only the key value pairs

#changing a value of a dictionary is the same process as adding new key values
alien1['color'] = 'green'
print(alien1['color'])
print("\n")

alien1['speed'] = 'slow'

if alien1['speed'] == 'slow':
    x_increment = 1
elif alien1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien1['x position'] = alien1['x position'] + x_increment
print(str(alien1['x position']))

#alien1 is moving over again
alien1['x position'] = alien1['x position'] + x_increment
print(str(alien1['x position']))

#if alien1 speed changes we'll have to make a new if statement again because of operation order

#removing key values

del alien1['color']
print(alien1) #color is gone
print("\n")

#excercises

persons1 = {'first_name':'tony','last_name':'nguyen'}
print(persons1)

persons1['age'] = 26
print(persons1['age'])
print(persons1['first_name'])
print(persons1['last_name'])

favorite_numbers = {'tony':2,'sam':3,'jen':4}
print(favorite_numbers)
print('tonys favorite number is ' + str(favorite_numbers['tony']))

vocab = {'string':'can be words or numbers\n','integer':'numbers; can be seen as a string as well\n'}
print(vocab['string'])
