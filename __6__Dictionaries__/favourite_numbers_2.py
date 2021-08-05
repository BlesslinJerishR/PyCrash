#favourite_numbers_2.py
#6.10

#import
from _0_AddOns.defs import *
from _6_Dictionaries.favourite_numbers import favourite_numbers
print(favourite_numbers)

favourite_numbers['ram'] = [favourite_numbers['ram'],3,7]
favourite_numbers['kalai'] = [favourite_numbers['kalai'],32,37]
favourite_numbers['jerry'] = [favourite_numbers['jerry'],5,47]
favourite_numbers['swetha'] = [favourite_numbers['swetha'],89,64]
favourite_numbers['deepika'] = [favourite_numbers['deepika'],23,67]
print(favourite_numbers)

#To print without [ ] 
for person,number in favourite_numbers.items():
	print(f"Person name : {person} \nFavourite numbers : {','.join(repr(bracket) for bracket in number)}") ###REPR###

nums = list_numbers(10)
print(nums)

