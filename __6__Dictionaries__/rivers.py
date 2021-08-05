#rivers.py
#6.5

#import
from favourite_languages import favourite_languages
from favourite_numbers import favourite_numbers

rivers = {
	'nile' : 'egypt',
	'narmadha' : 'India',
	'gangai' : 'India',
	'yamuna' : 'India',
}

for river,country in rivers.items():
	print(f"River : {river.title()} \nCountry : {country.title()}\n")

#6.6
#friends list from favourite numbers
friends_list = []
for friend in favourite_numbers.keys():
	friends_list.append(friend)

#friends list from favourite languages
for friend in favourite_languages.keys():
	friends_list.append(friend)

#final friends list
print(f"Friends are : {friends_list} ")

#To check whether a friend has voted or not
for friend in friends_list:
	if friend in favourite_languages.keys():
		print(f"Thank you for voting, {friend.title()}")
	else:
		print(f"{friend.title()}, Please Vote")

