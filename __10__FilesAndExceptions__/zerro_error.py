# ZeroDivisionError
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

try:
    div = num1 / num2
    print(div)
except ZeroDivisionError:
    print("This number is not divisible by 0")