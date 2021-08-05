#boolean
#5.1
#importing system
import sys

#importing random
import random
#importing cars
from _3_Lists.cars import *

if __name__ == '__main__':
	
	#Empty Lists 
	cars_check = []
	cars_final = []
	cars_title = []
	
	#Lists of cars to be checked
	cars_1 = ["benz","toyoto","bmw","audi","jaguar","kia"]
	cars_2 = "Fiat Honda Ford Hyundai Mitsubishi Nissan Renault Toyota Volkswagen"
	
	#join function for cars_1
	cars_1 = " ".join(cars_1)
	print(f"My cars : {cars_1}")
	
	#def for list_2_string
	def l2s(list):
		return " ".join(list)
	#cars_2
	print(f"New cars : {cars_2}")
	
	#cars_3
	cars_3 = f"{cars_1} {cars_2}"
	print(f"Total cars : {cars_3}")
	
	#converting a total words to list using split
	#split function
	cars_check = cars_3.split(" ")
	print(f"Cars temp : {cars_check}")
	
	#finalization with titles
	for car in cars_check:
		cars_final.append(car.title())
	print(f"Final cars list {cars_final}")
	cars_check = cars_final
	print(f"Cars : {cars_check}\n")
	
	#original cars
	for car in cars:
		cars_title.append(car.title())
	cars = cars_title
	#randomization of the cars check
	random.shuffle(cars_check)
	cars_2_check = cars_check
	
	#def for checking whether a car is in the list
	print(f"My cars : {cars}\n")
	print(f"Cars to check : {cars_2_check}\n")
	
	def cars_check():
		for car in cars:
			print(car)
			for car_check in cars_2_check:
				print(car_check)
				#print(f"Name of the car : {original_car}")
				#print(f"Whether this {original_car} car is in the List ? { all_car == original_car}\n")
	
	#checking the def
	#whether i own this car
	def cars_check():
		for car_check in cars_2_check:
			if car_check in cars:
				boolean = True;
				print(f"You own this car --> {car_check}")
				print(f"{car_check} in my cars ? {boolean}")
			else:
				boolean = False;	
				print(f"You do not own this car xx> {car_check}")
				print(f"{car_check} in cars ? {boolean}")
	
	#executing the def
	cars_check()
cars_2_check = ['Fiat', 'Benz', 'Toyoto', 'Nissan', 'Hyundai', 'Kia', 'Mitsubishi', 'Jaguar', 'Audi', 'Bmw', 'Volkswagen', 'Honda', 'Renault', 'Toyota', 'Ford']