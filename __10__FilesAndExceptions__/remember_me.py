# 10.13
import json
from try_remember import new_user
username = 'username.json'
with open(username, 'r') as ur:
    user = json.load(ur)
ques = input(f"Is this your user name ? {user}! 'y' or 'n' : ")
if ques == 'y':
    print(f'I remember you {user}')
    print('Welcome back')
elif ques == 'n':
    user = new_user()