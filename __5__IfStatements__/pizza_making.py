#pizza_making.py

#importing time for sleep
import time

requested_toppings = ["mushrooms", "extra cheese","macroni"]
if __name__ == '__main__':
	if 'mushrooms' in requested_toppings:
		print("Adding mushrooms.")
		time.sleep(2)
	if 'pepperoni' in requested_toppings:
		time.sleep(2)
		print("Adding pepperoni.")
	if 'extra cheese' in requested_toppings:
		time.sleep(2)
		print("Adding extra cheese.")
	
	time.sleep(2)
	print("\nFinished making your pizza!")	