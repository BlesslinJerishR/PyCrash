# 10.6
# 10.6
while True:
    try:
        num1 = int(input('Enter the first number : '))
        num2 = int(input('Enter the second number : '))
        add = num1 + num2
        print(add)
    except ValueError:
        print('Please, Enter a integer')

