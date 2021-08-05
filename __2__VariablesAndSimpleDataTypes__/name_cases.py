#2.3
first_name	=	"sarojini"
last_name	=	"retnamony"
full_name	=	f"{first_name} {last_name}"
personal_message = f"Hello, {full_name.title()} welcome to India"
print(personal_message)

#2.4
name_lower = full_name.lower()
name_upper = full_name.upper()
name_title = full_name.title()
print(f"\nlower case : {name_lower} \nUPPER CASE : {name_upper} \nTitle case : {name_title}")

#2.5 #2.6
quote 		= "Everyone has two lives, the second one starts when they realise they have only one"
author_name = "anonymous"
tabs		= "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
quote_final = f'Once a wise man said , "{quote} by \n{tabs}-{author_name.title()}'
print(quote_final)

#2.7
name_strip	= "        Hello Friend        "
print(f"origin : {name_strip}")
name_rstrip	= name_strip.rstrip()
name_lstrip	= name_strip.lstrip()
name_strip	= name_strip.strip()
print(f"rstrip : {name_rstrip}")
print(f"lstrip : {name_lstrip}")
print(f"strip : {name_strip}")


