#make a for loop to print the numbers list
numbers = list(range(1,21))
print(numbers)
for number in numbers:
    print(number)
print("\n")

#make and print a list of numbers 1-1,000,000 using a for loop
numbers = list(range(1,1000001))
#for number in numbers:
    #print(number)
#takes too long to print, commenting it

print(min(numbers))
print(max(numbers))
print(sum(numbers))

#make a list that hits only odd numbers
numbers = list(range(1,21,2))
print(numbers)

#make a list and cube it
numbers = []
for number in range(1,11):
    cubed = number**3
    numbers.append(cubed)
print(numbers)

numbers = list(range(3,33,3))
print(numbers)
