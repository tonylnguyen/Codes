#using a while loop in a dictionary

unconfirmed_users = ['tony','sam','niko']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print('Verifying User: ' + current_user.title())
    confirmed_users.append(current_user)

print("\nThese users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print(unconfirmed_users)
print("-"*20)
#-------------------------------------------
#removing doubles from a list
confirmed_users.append('niko')
confirmed_users.append('niko')
confirmed_users.append('niko')
print(confirmed_users)

while 'niko' in confirmed_users:
    confirmed_users.remove('niko')
print(confirmed_users)

#filling dictionary/list with a user input
student_schools = {}
active_student = True

while active_student:
    name = input("What is your name? \n\t>")
    school = input("What school do you go to? \n\t>")

    student_schools[name] = school
    repeat = input("Is there anyone else that attends school? yes/no \n\t>")
    if repeat == 'no':
        active_student = False

print(student_schools)
for student, school in student_schools.items():
    print(student.title() + " goes to " + school +'.')

print('-'*20)
#-------------------------------------------
ramen_orders = ['kuro (K)','shiro (S)','chasu kuro (CK)','shiro (SLT)','kuro (K)','kuro (K)','kuro (K)','kuro (K)']
made_ramen = []

while 'kuro (K)' in ramen_orders:
    ramen_orders.remove('kuro (K)')

while ramen_orders:
    cooked = ramen_orders.pop()
    made_ramen.append(cooked)

    print(cooked.title() + " has been made.")

work_places = {}
working = True

while working:
    name = input("What is your name? \n >")
    places = input('Where do you work? \n >')

    work_places[name] = places

    asking = input("Is there anyone else? (yes/no)\n >")
    if asking == 'no':
        working=False

for name, place  in work_places.items():
    print(name + ' works at ' + place +'.')
