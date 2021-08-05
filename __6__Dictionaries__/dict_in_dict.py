#dict_in_dict.py

spersons = {
	'sarojini' : {
	'first_name': 'sarojini',
	'last_name': 'retnamony',
	'age': '50',
	'place': 'kanyakumari',
	},

	'blessy' : {
	'first_name': 'blessy',
	'last_name': 'jenila',
	'age': '28',
	'place': 'chennai',
	},

	'ceo' : {
	'first_name': 'sridhar',
	'last_name': 'vembu',
	'age': '48',
	'place': 'thenkasi',
	}
}

if __name__ == '__main__':
	print(persons)
	for person, info in persons.items():
		print(f"\nName : {person.title()} \nFull name : {info['first_name'].title()} {info['last_name'].title()}  \nAbout : {info}")
