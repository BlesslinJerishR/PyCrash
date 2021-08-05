from _0_AddOns.defs import random_names
dogs = random_names(3)

def write_dogs():
    with open('dogs.txt', 'w') as dw:
        for dog in dogs:
            dw.write(f'{dog}\n')

write_dogs()
