# importing
from _0_AddOns.defs import random_names


def greet_list(list):
    """Simple greeting of messages in a list"""
    for user in list:
        print(f'Hello {user}')


names = random_names(5)
greet_list(names)
