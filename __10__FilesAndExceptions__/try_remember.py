import json


def new_user():
    user = input("What is your name ? ")
    return user


username = 'username.json'
user = new_user()
if '__init__' == 'main':
    try:
        with open(username, 'r') as ur:
            user_data = json.load(ur)
        print(f'I remember you {user_data}')
    except FileNotFoundError:
        print(f'We will remember when you come back {user}')
