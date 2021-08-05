#glossary.py
#6.3

glossary = {
	'variable' : 'used to store and reuse a data',
	'loops'	   : 'used to execute certain times',
	'range'	   : 'to print within a certain boundary',
	'function' : 'to reuse a certain method',
	'get'	   : 'to get a key value for uncertain pairs',
}

if __name__ == '__main__':
	#import
	from favourite_languages import favourite_languages
	print()
	print(glossary)
	print(f"Variable : {glossary['variable']}")

	#for loop in dictionary
	#items
	#items = key + values
	for word, function in glossary.items():
		print(f"\nWord : {word}")
		print(f"Function : {function}")

	for name, favlang in favourite_languages.items():
		print(f"\nThe favourite language of {name.title()} is {favlang.title()} ")

	for name in favourite_languages.keys():
		print(f"\n{name}")

	friends = ['ram', 'sara']

	for name in favourite_languages.keys():
		print(name.title())
		if name in friends:
			language = favourite_languages[name].title()
			print(f"\t{name.title()}, I see you love {language}!")

	print()
	if 'Blesslin' not in favourite_languages.keys():
		print("Blesslin, please take our poll")
	else:
		print("Thanks for the poll")
	print()
	for key, value in favourite_languages.items():
		if 'python' in value:
			print(f"{value}, you are the best language")
	print()
	#keys
	for friend in sorted(favourite_languages.keys()):
		print(f"{friend.title()}, Thanks for taking the poll")

	#values
	print("\nThe language consist in polls are: ")
	for language in sorted(favourite_languages.values()):
		print(f"{language.title()} is in the poll")

	#set
	print("\nThe language without repetition are: ")
	for language in set(favourite_languages.values()):
		print(language)

	languages = {'java','c','c++','python','java'}

	#set
	print(languages)