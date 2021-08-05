squares = []
for number in range(1,11):
	#squares.append(number**2)
	#or
	square = number**2
	squares.append(square)
print(squares)

#statistical functions 
print(f"The maximun of the numbers is : {max(squares)}")
print(f"The minimum of the numbers is : {min(squares)}")
print(f"The sum of the numbers is : {sum(squares)}")

#list comprehension
print("using list comprehension")
squares = [number**2 for number in range(1,20)]
print(squares)