# 9.13
import random


class Die:
    def __init__(self, side=6):
        self.side = side

    def roll_die(self):
        return random.randint(1, self.side)


print('\n6 sided Die\n')
for die in range(1, 10+1):
    dice = Die(6)
    roll_dice = dice.roll_die()
    print(f'Roll {die} : {roll_dice}')

print('\n10 sided Die\n')
for die in range(1, 10+1):
    dice = Die(10)
    roll_dice = dice.roll_die()
    print(f'Roll {die} : {roll_dice}')

print('\n20 sided Die\n')
for die in range(1, 10+1):
    dice = Die(20)
    roll_dice = dice.roll_die()
    print(f'Roll {die} : {roll_dice}')
