# To open pi file

pi_file = 'pi_millions.txt'
with open(pi_file) as pi:
    pi_digits = pi.readlines()
    pi_string = ""
    for digits in pi_digits:
        pi_string += digits.strip()
    # print(pi_string)

birthday = input("Enter your birthday (dd/mm) : ")
if birthday in pi_string:
    print("Your Birthday is in pi")
else:
    print("Your birtday is not in pi")
