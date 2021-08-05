import json
username = 'username.json'


def write_user():
    user = input("What is your name ? ")
    with open(username, 'w') as uw:
        json.dump(user, uw)
    return user


user = write_user()
print(f'We will remember when you come back {user}')