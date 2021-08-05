# importing
from _0_AddOns.defs import *

# removing duplicates
animals = random_animals(5)
animals = repeat_items(animals)

animals_unique = set(animals)
print(list(animals_unique))
