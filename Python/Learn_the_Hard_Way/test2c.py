sentence = 'Define a function that returns the number of vowels in a given string.'

def counter(string):
    data = list(string)
    vowels = ['a','e','i','o','u']
    vowel_count  = []

    for i in data:
        if i in vowels:
            vowel_count.append(i)
    return len(vowel_count)

print(counter(sentence))
