#glossary_2.py
#6.4

#import
from glossary import glossary
from _0_AddOns.defs import *

glossary_2  = {
	'items' : 'This method returns both the key and values',
	'keys'	: 'This method returns only the key values',
	'values' : 'This method returns only the values',
	'set'	: 'This method returns the values without repetition',
	'random' : 'This package consists of random functions',
}
print(f"Glossary 1 : {glossary} ")
glossary = dict_merge(glossary,glossary_2)
print(f"\nGlossary 2 before merging :  {glossary_2}")
print(f"\nGlossary 2 after merging : {glossary} ")

#items in glossary
for function_name,function_uses in glossary.items():
	print(f"\nFunction : {function_name}")
	print(f"Use : {function_uses}")

