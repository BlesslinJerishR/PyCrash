# cities.py
# 6.11
cities = {
	'chennai' : { 
	'country' : 'India',
	'population' : '70.9L',
	'fact' : "Don't get into fight with anyone", } ,
	'kanyakumari' : { 
	'country' : 'India',
	'population' : '29,761',
	'fact' : 'Try Yellow Baji and Parota + Beef'} ,
	'coimbatore' :  { 
	'country' : 'India',
	'population' : '16L',
	'fact' : 'Cool Climate'} 
}

# delhi_dict = {'delhi' : {
# 	'country' : 'India',
# 	'population' : '1.9Cr',
# 	'fact' : 'Kejrival rockz',}
# 	}

# cities.update(delhi_dict)
# print(cities)
# 6.12

cities.update({'delhi' : {
	'country' : 'India',
	'population' : '1.9Cr',
	'fact' : 'Kejrival rockz',}
	})
print(cities)

#for
for city, facts in cities.items():
	print(f"\nName of the city : {city.title()} ")
	print(f"{city} city is located in {facts['country']}")
	print(f"{city} city consists of {facts['population']} people ")
	print(f"One fact about the city is >>> {facts['fact']} ")
