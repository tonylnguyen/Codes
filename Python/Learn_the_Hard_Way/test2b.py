list1 = ['cat','dog','rat','mouse','bird','cat','dog','snake','dog','Tony']
list2 = ['cat','dog','rat','yellow','blue','green','purple','red']

def same(list1,list2):
    new_list = []
    for loop in list1:
        if loop in list2:
            new_list.append(loop)
    for loop in new_list:
        if loop in new_list:
            new_list.pop(new_list.index(loop))
    print new_list
same(list1,list2)


#when looping through a list, don't modify it. if you shift it, it could change the code


#def same(list1,list2):
#    new_list = []
#    for loop in list1:
#        if loop in list2:
#            new_list.append(loop)

#    another_list = []
#    for loop in another_list:
#        if loop in new_list
#            new_list.pop(new_list.index(loop))
#    print new_list
#same(list1,list2)
