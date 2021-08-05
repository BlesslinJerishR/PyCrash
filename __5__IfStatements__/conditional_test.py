#5.2
#conditonal test

#imports
from boolean import cars, cars_2_check

print(cars)
print(cars_2_check)

print(cars[0] == cars_2_check[1])
print(cars[0].title() == cars_2_check[1])
print(cars[0] == cars_2_check[1].lower())

number_1 = list(range(0,10))
number_2 = list(range(1,11))
print(number_1)
print(number_2)
print(sum(number_1) > sum(number_2))

if len(number_1) and len(number_2) == 10:
	print("Yes")
else:
	print("no") 
	

if number_1[1] in number_2:
	print(True)
else:
	print(False)

if number_1[0] not in number_2:
	print(True)
else:
	print(False)

