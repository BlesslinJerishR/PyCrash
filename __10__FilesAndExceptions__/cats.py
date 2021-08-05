from _0_AddOns.defs import random_names
cats = random_names(3)

def write_cats():
    with open('cats.txt', 'w') as cw:
        for cat in cats:
            cw.write(f'{cat}\n')

write_cats()