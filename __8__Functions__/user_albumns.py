# 8.8
users_albumn = {
        'Artist': [],
        'Albumn': [],
    }
while True:
    artist = input('Who is your favourite artist ? ')
    albumn = input('Which is your favourite albumn ? ')
    users_albumn['Artist'].append(artist)
    users_albumn['Albumn'].append(albumn)
    exit = input("Would you like to continue 'yes' or 'no' ? ")
    if exit == 'no':
        # print(f'Your favourite artist is {artist} and favourite albumn is {albumn}')
        break
print(users_albumn)

