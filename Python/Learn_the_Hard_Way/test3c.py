lista = ['a','b','c']
list1 = [1,2,3]

def combine_lists(lista, list1):
    combined = []
    counter = 0
    while counter < len(lista):
        combined.append(lista[counter])
        combined.append(list1[counter])
        counter = counter + 1

    return combined

print combine_lists(list1, lista)
