
def print_this(i, limit):
    numbers = []
    counter = len(numbers)

    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now: :", numbers
        print "At the bottom i is %d" % i


        print "The numbers: "
        for num in numbers:
            print num

print_this(8,9)
