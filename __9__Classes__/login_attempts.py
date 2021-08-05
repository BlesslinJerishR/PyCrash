# 9.5

from users import User

j = User('James', 'Bond', 1)
print(f'First name : {j.first_name} \nLast name : {j.last_name} \nLogin attempts : {j.login_attempts}')
j.increment_login_attempts()
print(f'Login attempts after increment : {j.login_attempts}')
j.reset_login_attempts()
print(f'Login attempts after reset : {j.login_attempts}')

for num in range(8):
    j.increment_login_attempts()
print(f"Login attempts after updating : {j.login_attempts}")
j.reset_login_attempts()
print(f'Login attempts after reset : {j.login_attempts}')
