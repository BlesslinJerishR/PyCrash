#admin.py
#5.8
#import
import sys
from _0_AddOns.defs import *

#user list
users = ["jade","matt","damon","depp","admin",]
list_titles_permanent(users)

# list_clear(users)
print(users)

#Looping through the list of users
for user in users:
	if user == "admin".title():
		print(f"Welcome {user} , Would you like to see today's report ?")
	else:
		print(f"Greeting {user}")

#5.9
#To Check whether a list is empty
if len(users)==0:
		print("We need to find more users")

