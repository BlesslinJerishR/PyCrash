import json
from _0_AddOns.defs import list_numbers
file = 'numbers.json'
number = list_numbers(10)
with open(file, 'w') as jr:
    json.dump(number, jr)