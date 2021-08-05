# 9.14
import random

from _0_AddOns.defs import list_numbers, list_alphabets, list_to_str_no_comma

numbers = list_numbers(9)
numbers.append(random.randint(1, 9))
letters = list_alphabets(5)


def number_selector():
    """Algorithm for lottery number selection"""
    number_winner = []
    for num in range(4):
        number_4 = random.choice(numbers)
        number_winner.append(number_4)
    return list_to_str_no_comma(number_winner)
    pass


def letter_selector():
    """Algorithm for lottery letter selection"""
    letter_winner = []
    for num in range(4):
        letter_4 = random.choice(letters)
        letter_winner.append(letter_4)
    return "".join(letter_winner)
    pass


if __name__ == '__main__':
    print(f'The Numbers are : {numbers}')
    print(f'The letters are : {letters}')
    # number_selector()
    # letter_selector()
    print(f'\nThe winner of number series are :- ')
    print(number_selector())
    # for num in number_winner:
    #     print(num, end="")

    print(f'\nThe winner of letter series are :- ')
    print(letter_selector())
    # for letter in letter_winner:
    #     print(letter, end="")
