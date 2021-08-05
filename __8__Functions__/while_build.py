# importing
def full_name_title(first_name, last_name):
    return f"{first_name.title()} {last_name.title()}"


while True:
    print('Please, Tell me your name: ')
    print("Enter 'q' anytime to quit")

    f_name = input('First name : ')
    if f_name == 'q':
        print('Thank you')
        break
    l_name = input('Last name : ')
    if l_name == 'q':
        print('Thank you')
        break
    full_name = full_name_title(f_name, l_name)
    print(f"Hello {full_name}\n")
