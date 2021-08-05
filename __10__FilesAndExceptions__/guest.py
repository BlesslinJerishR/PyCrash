# 10.3
guest = 'guest.txt'
with open(guest, 'a') as guest_records:
    for names in range(5):
        name = input('Enter your name : ')
        guest_records.write(f'{name}\n')