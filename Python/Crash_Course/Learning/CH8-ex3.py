#returning values
def formatted (first_name, last_name):
    full_name = first_name +" " + last_name #defines the full name
    return full_name.title() #returns the value of full name

musician = formatted('stevie', 'wonder') #musician stores the value of the function formatted
print(musician)

#optinal arguments ie Middle Names

def complete_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name +" " + last_name
    return full_name.title()

tony = complete_name('tony','nguyen','lam') #creating an optional argument (lam)
print(tony)
print(musician) #notice how msucian still printed even with no middle name

#using return to store dictionaries (with optional argument )
print('-'*20)
def user_bio(first_name, last_name, age = ''):
    person = {'first: ': first_name, 'last: ' :last_name}
    if age:
        person['age'] = age
    return person

niko = user_bio('niko','nobida', age = 24)
tony = user_bio('tony','nguyen')
print(niko)
print(tony)
print('-'*20)
#using functions and while loops

def work_place(name, place):
    employment = {'Name: ': name.title(), 'Place: ': place.title()}
    return employment
print('-'*20)
while True:
    print('\nPlease enter your name and where you work.')
    print('type done, when you are finished')

    f_name = input('Name \n >')
    if f_name == 'done':
        break
    f_place = input('Work \n > ')
    if f_place == 'done':
        break

    name_work = work_place(f_name,f_place)
    print(name_work)

print('-'*20)
#excersies

def city_place (city, place):
    location = city.title() + ', ' + place.title()
    return location

paris = city_place('paris','france')
sf = city_place('san francisco','united states')
cabo = city_place('cabo san lucas', 'Mexico')
print(paris)
print(sf)
print(cabo)


#slightly different from the excersies in the book
def song(song_name, song_artist, featuring = ''):
    album = {'Name': song_name, 'By':song_artist}
    if featuring:
        album['Ft.'] = featuring
    return album


track1 = song('Kissed a girl','katy Perry')
track2 = song('renegades','x amassenders')
track3 = song('titanium','calvin haris','sia')

print(track1)
print(track2)
print(track3)

while True:
    print('\nType in your artist and song. type done when you are finished.\n')
    user_song_name = input('Song Name \n >')
    if user_song_name == 'done':
        break
    user_song_artist = input('Artist Name \n >')
    if user_song_artist == 'done':
        break
    user_featuring = input('Featuring (type enter if none) \n >')
    if user_featuring =='done':
        break
    user_song = song(user_song_name,user_song_artist,user_featuring)
    print(user_song)

print('-'*20)
