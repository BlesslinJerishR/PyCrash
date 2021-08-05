banned_users = ["ramesh","rajesh","vinoth","ram","kalai"]
users = ["tejas","kalai"]

#for loop
for user in users:
	#in
	if user in banned_users:
		print(f"{user.title()}, You can not post right now. Please contact admin.") 
	#not in 
	if user not in banned_users:
		print(f"{user.title()}, You can post right now. Thank you!") 
