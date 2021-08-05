#ordinal_numbers.py
#5.11

#import
import sys
from _0_AddOns.defs import *

ordinal_numbers = list_numbers(9)
zero_remover(ordinal_numbers)
print(ordinal_numbers)
for number in ordinal_numbers:
	if number  == 1:
		print(f"{number}st")
	elif number  == 2:
		print(f"{number}nd")
	elif number   == 3:
		print(f"{number}rd")
	else:
		print(f"{number}th")

