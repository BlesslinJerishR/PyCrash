#importing file from another folder
#importing system
import sys
#importing
from _3_Lists import cars
from _2_VariablesAndSimpleDataTypes.full_name import *
print(cars)

#list
cars_new = []

#if condition
for car in cars:
	if car == 'bmw':
		cars_new.append(car.upper())
	else:
		cars_new.append(car.title())
		pass
print(cars_new)

#True condition
print(first_name == "blessy")
#not equal to
print(last_name != "jenila")
