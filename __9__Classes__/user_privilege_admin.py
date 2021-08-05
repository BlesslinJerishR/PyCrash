import time
import random

from _0_AddOns.defs import tick, cross


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


class Admin(User):
    """To get admin information"""
    admin_actions = ['can add post', 'can delete post', 'can ban user', 'can comment posts', 'can post pictures']

    def __init__(self, fname, lname, login_attempts=0, *privileges):
        super().__init__(fname, lname, login_attempts)
        self.privileges = privileges
        self.privileges_instance = Privileges()

    def shuffle_privileges(self):
        current_privileges = []
        for privilege in self.privileges:
            current_privileges.append(privilege)
        random.shuffle(current_privileges)
        return current_privileges

    def show_privileges(self):
        print(f"The admin {self.full_name()} can do the following actions : -")
        for privilege in Admin.shuffle_privileges(self):
            if privilege in Admin.admin_actions:
                time.sleep(1)
                print(f'{privilege}', end=" ")
                time.sleep(1)
                print(tick())
            else:
                time.sleep(1)
                print(f'{privilege}', end=" ")
                time.sleep(1)
                print(cross())
                time.sleep(1)

    # def r_privileges(self):
    #     return Admin.shuffle_privileges(self)


class Privileges:
    """Class for only privileges"""
    def __init__(self, *privileges):
        self.privileges_instance = privileges

    def current_privileges(self):
        current_privileges = []
        for privilege in self.privileges_instance:
            current_privileges.append(privilege)
        return current_privileges

    def desc_privileges(self):
        for privilege in Privileges.current_privileges(self):
            if privilege in Admin.admin_actions:
                time.sleep(1)
                print(f'{privilege}', end=" ")
                time.sleep(1)
                print(tick())
            else:
                time.sleep(1)
                print(f'{privilege}', end=" ")
                time.sleep(1)
                print(cross())
                time.sleep(1)
