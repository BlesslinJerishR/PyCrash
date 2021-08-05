#format f
#variables
first_name	= "blessy"
last_name	= "jenila"
full_name	= f"{first_name} {last_name}"

if __name__ == '__main__':
	print(full_name)
	print(f"Hello , {full_name.title()}")
	
	f_variable = f"{full_name.title()}"
	print(f"Hello {f_variable}. I am from a variable")
	
	#format old
	format_old = "Hi {} {}".format(first_name.title(), last_name.title())
	print(format_old)	