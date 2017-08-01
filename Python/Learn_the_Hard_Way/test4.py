# the first code i wrote returned number of letters not words. This is fixing it.
def number_of_words(f):
    words = f.split()
    return len(words)


a = 'fjkd fdska fjdlasa'

print number_of_words(a)
