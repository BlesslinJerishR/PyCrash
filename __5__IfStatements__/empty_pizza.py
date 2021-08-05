#empty_pizza.py
#import
from pizzeria import requested_toppings
import time

print(requested_toppings)
# requested_toppings = []
print(requested_toppings)

#To check if a List is empty
if requested_toppings:
	for topping in requested_toppings:
		time.sleep(1)
		print(f"Adding {topping} ")
	print("Pizza ready")
else:
	time.sleep(1)
	print("Are you sure you want a plain pizza ?")

