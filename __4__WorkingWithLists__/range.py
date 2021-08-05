#4.3
#for loop
for number in range(1,21):
	print(number)
#using list comprehension
twenty = [number for number in range(1,21)]
print(f"List : {twenty}")

#4.4
one_million = [million for million in range(1,10_00_000+1)]

#caution : takes some secs
#print(one_million)
for one in one_million:
	#caution : takes some secs
	#print(f"number : {one}")
	break

#4.5
print(f"Min of one million : {min(one_million)}")
print(f"Max of one million : {max(one_million)}")
print(f"Sum of one million : {sum(one_million)}")

#4.6
odd_numbers = list(range(1,20+1,2))
print(f"Odd numbers : {odd_numbers}")
for number in odd_numbers:
	break
	print(number)

#4.7
three_table = list(range(3,30,3))
print(f"Multiples of three : {three_table}")
for number in three_table:
	break
	print(number)

#4.8
cubes =[]
for number in range(1,10+1):
	cube = number**3
	cubes.append(cube)
print(f"Cubes using append: {cubes}")

#4.9
cube_comprehension = [cube**3 for cube in range(1,10+1)]
print(f"Cubes using comprehension : {cube_comprehension}")