#favourite_languages.py

favourite_languages = {
	'sara' : 'c',
	'dora' : 'c++',
	'jerry' : 'python',
	'jenkins' : 'java',
	'jeyhar' : 'python'
}
if __name__ == '__main__':
	print(favourite_languages)
	sara_favlang = favourite_languages['sara'].title()
	print(f"Sara's favourite language is {sara_favlang} ")

	#get method
	favlang_points = favourite_languages.get('points','Points not found')
	print(favlang_points)