#using a function to pass a list
usernames = ['tony','sam','niko','jen']

def hello_names(names):
    for name in names:
        print('Hello ' + name.title())

hello_names(usernames)
print('-'*20)


#using a while loop/ for loop inside a function

def final_exam(unfinished,finished):
    print("\nThese people are taking a test:")
    for test in unfinished:
        print(str(test).title())
    while unfinished:
        taking_test = unfinished.pop()
        finished.append(taking_test)
    print("\nThese people are done: ")
    for people in finished:
        print(people.title())

unfinished = ['carry','ted','niko','jen']
finished = []

final_exam(unfinished[:],finished) #use the [:] if we want to make a copy of the list but still want to move items

print(unfinished)
print(finished)
print('-'*20)

#exersices

magicians = ['edward','henry','mary','francis']

def show_magicians(list):
    print("Here are our magicians!")
    for preformers in list:
        print(preformers.title())

show_magicians(magicians)
print('\n')
def great_magicians(list):
    for preformers in list:
        print("Please welcome the Great " + preformers.title() + ".")
great_magicians(magicians)
print('\n')
#popping and calling

def pop_magicians(list, new_list):
    while list:
        pop_magic = list.pop()
        new_list.append(pop_magic)
    print(list)
    print(new_list)

on_stage = []

pop_magicians(magicians[:],on_stage)
print(magicians)
