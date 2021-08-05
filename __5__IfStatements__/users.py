#profile.txt
#5.10

#import
import sys
from _0_AddOns.defs import *


current_users = ["ramesh","rajesh","vinoth","ram","kalai","Tejas"]
new_users = ["rocky","bala","praveen","pranav","kalai","ram","TEJAS"]

for user in list_titles_permanent(new_users):
	if user in list_titles_permanent(current_users):
		print(f"{user} username is not available, please enter another username.")
	else:
		print(f"{user} username is available.")
