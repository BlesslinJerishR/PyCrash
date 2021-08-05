# 9.3

class User:
    """Info about users"""

    def __init__(self, fname, lname, login_attempts=0):
        self.first_name = fname
        self.last_name = lname
        self.login_attempts = login_attempts

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def about(self):
        print(f"My first name is {self.first_name}")
        print(f"My last name is {self.last_name}")

    def greet_user(self):
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = int
        self.login_attempts = 0


if __name__ == '__main__':
    user_1 = User('blesslin', 'jerish')
    user_1.about()
    user_1.greet_user()

    print()

    user_2 = User('blessy', 'jenila')
    user_2.about()
    user_2.greet_user()
