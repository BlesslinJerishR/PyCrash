#pizzeria.py
#importing
import sys
import time
import random
from pizza_making import requested_toppings

#def variable requested_toppings
#def requested_toppings_var():
	# requested_toppings_new = requested_toppings[:]
	# print(requested_toppings_new)
	# return requested_toppings_new
if __name__ == '__main__':
	requested_toppings.append("green peas")
	requested_toppings.append("chilli")
	print(requested_toppings)
	random.shuffle(requested_toppings)
	
	for topping in requested_toppings:
		time.sleep(2)
		print(f"Adding {topping} to pizza")
		if topping == "green peas":
			print("Sorry, we ran out of green peas")
	time.sleep(2)
	print("Pizza Ready")
else:
	requested_toppings = ['mushrooms', 'extra cheese', 'macroni', 'green peas', 'chilli']