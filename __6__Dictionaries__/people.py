#people.py
#6.7

persons = [
	{
	'first_name': 'sarojini',
	'last_name': 'retnamony',
	'age': '50',
	'place': 'kanyakumari',
	},
	{
	'first_name': 'blessy',
	'last_name': 'jenila',
	'age': '28',
	'place': 'chennai',
	},
	{
	'first_name': 'sridhar',
	'last_name': 'vembu',
	'age': '48',
	'place': 'thenkasi',
	}
]


print(persons)

#Dictionary
# for user, info in persons.items():
# 	print(f"Name : {user}.title() \nFirst Name : {info['first_name'].title()} \nLast Name : {info['last_name'].title()} \nFull Name : {info['first_name'].title()} {info['last_name'].title()}")

#List
for person in persons:
	print(f"Name : {person['first_name'].title()} {person['last_name'].title()}\nFirst Name : {person['first_name'].title()} \nLast Name : {person['last_name'].title()}")