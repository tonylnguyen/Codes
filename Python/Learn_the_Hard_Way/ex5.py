name = 'Tony Nguyen'
age = 27
height = 64 #inches
weight = 135 #lb
eyes = 'brown'
teeth = 'white'
hair = 'black'

inches_to_cm = height * 2.54
lb_to_kg = weight * 0.453592

print('Lets talk about %s.' %name)
print("He's %d cm tall." %inches_to_cm)
print("He's %d kg heavy." %lb_to_kg)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." %(eyes, hair))
print("He's teeth are normally %s depending on the coffee." %(teeth))

print('If I add %d, %d, and %d I would get %d.' %(age, height, weight, age + height + weight))
