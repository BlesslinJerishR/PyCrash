#pets.py
#6.8

pets_0 = {
	'name' : 'goldy',
	'type' : 'fish',
	'owner' : 'jim',
}

pets_1 = {
	'name' : 'doggy',
	'type' : 'dog',
	'owner' : 'juri',
}

pets_2 = {
	'name' : 'toro',
	'type' : 'horse',
	'owner' : 'jian',
}

pets = [pets_0,pets_1,pets_2]
print(pets)
# print(f"{pets_0}\n{pets_1}\n{pets_2}")
print()
for pet in pets:
	print(f"Name of the pet : {pet['name'].title()} \nType of the pet : {pet['type'].title()} \nName of the owner : {pet['owner'].title()}\n")