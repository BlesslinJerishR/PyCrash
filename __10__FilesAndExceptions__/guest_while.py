# 10.4

guest_txt = 'guest_books.txt'
with open(guest_txt, 'a') as guests:
    ask = True
    names = 0
    guests.write("Today's Guests\n")
    while ask:
        name = input('Enter your name : ')
        names += 1
        guests.write(f'{name}\n')
        if names == 3:
            ask = False
    guests.write("\n")
