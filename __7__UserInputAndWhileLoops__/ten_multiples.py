# ten_multiples.py
# 7.3
num = input("Enter a number : ")
num = int(num)

if num % 10 == 0:
    print(f"The number {num} is a multiple of 10")
else:
    print(f"The number is {num} not a multiple of 10")