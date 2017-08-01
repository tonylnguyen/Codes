import urllib

def read_file():
    open_file = open('/Users/tonynguyen/Desktop/Codes/Udacity/Python/Curse_words.txt')
    read_contents = open_file.read()
    print(read_contents)
    open_file.close()
    check_curse(read_contents)

def check_curse(check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("You have a curse word.")
    else:
        print("Your document is clean.")

read_file()
