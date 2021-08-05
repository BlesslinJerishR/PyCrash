#aliens.py

#list to store aliens
aliens = []

#To create 30 aliens
for alien_nos in range(30):
	new_alien = {
	'color' : 'green',
	'speed' : 'slow',
	'points' : 5,
	}
	aliens.append(new_alien)

#First five aliens
print(f"First five aliens :-")
for alien in aliens[:5]:
	print(f"\n {alien} ")

#Total Aliens
print(f"\nTotal number of aliens are : {len(aliens)} ")

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
		pass
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
for alien in aliens:
	print(f"\n {alien} ")
	pass