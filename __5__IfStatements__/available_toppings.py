#available_toppings.py
#import
from pizzeria import requested_toppings
import random

available_toppings = ['mushrooms', 'extra cheese', 'macroni','french fries','spicy corn']
random.shuffle(requested_toppings)
random.shuffle(available_toppings)
print(f"requested_toppings : {requested_toppings} ")
print(f"available_toppings : {available_toppings} ")

#checking whether the requested toppings is in available topping
for topping in requested_toppings:
	if topping in available_toppings:
		print(f"Adding {topping} to Pizza")
	else:
		print(f"Sorry {topping} topping is not available right now ")
print("Pizza ready")