#favlang.py

from favourite_languages import favourite_languages

favlang = {'sara': ['c','python','c#'], 
			'dora': ['c++','java'], 
			'jerry': ['python'], 
			'jenkins': ['java','swift'],
			'jeyhar': ['python','ruby'],}
print(favourite_languages)

for user ,languages in favlang.items():
	if(len(languages) == 1):
		print(f"\n{user}'s favourite language is ")
		for language in languages:
			print({language})
	else:
		print(f"\n{user}'s favourite languages are : ")
		for language in languages:
			print({language})



