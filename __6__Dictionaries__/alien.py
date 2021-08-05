#alien.py
#6
#dictionary

#INITIALIZING VALUES IN DICTIONARIES
alien_0 = {
	'color':'green',
	'points':5
}

print(alien_0)
print(alien_0['color'])
print(alien_0['points'])

green_points = alien_0['points']
print(f"Congratulations, you have just earned {green_points} points")

alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)

#empty dictionaries >> automatic generation of values or input by users
alien_1 = {}
alien_1['color'] = 'yellow'
alien_1['points'] =  10
print(alien_1)

#CHANGING VALUES IN DICTIONARIES
print(f"The color of alien 0 is {alien_0['color']} ")
alien_0['color'] = 'red'
print(f"changed color of alien 0 is {alien_0['color']} ")

alien_1['x-position'] = 0
alien_1['y-position'] = 25

alien_0['speed'] = 'slow'
alien_1['speed'] = 'medium'

print(alien_0)
print(alien_1)

print(f"Orginal X position of alien #0 is : {alien_0['x-position']} ")
print(f"Orginal X position of alien #1 is : {alien_1['x-position']} ")


#To move alien to the right
#alien 0
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#It must be a Fast alien
	x_increment = 3

alien_0['x-position'] = alien_0['x-position'] + x_increment 

#alien 1
if alien_1['speed'] == 'slow':
	x_increment = 1
elif alien_1['speed'] == 'medium':
	x_increment = 2
else:
	#It must be a Fast alien
	x_increment = 3

alien_1['x-position'] = alien_1['x-position'] + x_increment 

print(f"X position of alien #0 after increment is : {alien_0['x-position']} ")
print(f"X position of alien #1 after increment is : {alien_1['x-position']} ")


#del in dictionary
del alien_0['points']
print(alien_0)
