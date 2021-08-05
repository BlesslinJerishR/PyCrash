#cars list
cars = ["benz","toyoto","bmw","audi","jaguar","kia"]

if __name__ == '__main__':	
	print(cars)
	cars.reverse()
	print(cars)
	#temporary sort
	print(sorted(cars))
	print(f"Temp : {sorted(cars)}")
	print(f"Check : {cars}")
	#permanent sort
	cars.sort()
	print(f"Permenant : {cars}")
	cars.sort(reverse=True)
	print(f"Reverse : {cars}")
	
	#length of a list
	list_length = len(cars)
	print(list_length)
	