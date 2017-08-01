#make a guest list

guest_list = ['rose tyler','dr. who','clara olwald','the master']
guest_list.append('donna noble')
guest_list.insert(2, 'martha jones')
print(guest_list)
lost_memory = guest_list.pop(5)
print(guest_list)
print(lost_memory.title() + 'had her memory wiped. Take her off the list.')
del guest_list[0]
print(guest_list)
guest_list.remove('the master')
print(guest_list)
