
first = raw_input("What is your first name? \n>").upper()
last = raw_input("What is your last name? \n>").upper()
length = len(first.strip() + last.strip())

print("\nYour name is %s %s has %d letters." % (first, last, length))


def capitalizeAndCount(first_name, last_name):
    print("\nYour name is %s %s." % (first_name, last_name))
    print("Your first name is %d letters long and your last name is %d letters long." % (
        len(first_name), len(last_name)))
capitalizeAndCount(first, last)
