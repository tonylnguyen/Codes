#store a persons name in a variable and print it
message = "I'm an idiot that accidently deleted all code files. Now I have to start over."
print(message)

#store a person's name in a variable and print it in .upper() .lower() .title() case
person = 'toNY'
print(person.title())
print(person.upper())
print(person.lower())

#practice using "" and '' within each other
print("Marie the Queen of France once said, 'Let them eat cake!'")
#note we learned in Learn the Python the Hard way that """ also works too

#repeat but this time store the message and person in a variable
message2 = "I'm so cold Jack."
famous_person = 'Rose DeWitt Bukater'
print(famous_person + ' once said, ' + "'" + message2 + "'")

#practice .lstrip() .rstrip() .strip() \n \t
name2 = "  tony     "
print(name2)
print(name2.lstrip()) #strips all the white space on the left
print(name2.rstrip()) #strips all the white space on the right
print(name2.strip()) #strips all white space
print("\t TAB \n now on a new line")
