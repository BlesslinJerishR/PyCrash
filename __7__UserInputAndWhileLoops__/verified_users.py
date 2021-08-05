# importing
from _0_AddOns.defs import random_names

# verification
unverified_users = random_names(6)
verified_users = []
# To verify users
while unverified_users:
    user = unverified_users.pop()
    print(f'Verifying user --> {user.title()} \u2713')
    verified_users.append(user)
# To view all verified users
print('The following users have been verified : ', end=" ")
for user in range(len(verified_users) - 1):
    print(f'{verified_users[user]}', end=", ")
print(f'{verified_users[-1]} .')
