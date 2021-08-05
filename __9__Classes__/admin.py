# 9.7
# 9.8
# 9.12

import random
import time

from _0_AddOns.defs import tick, cross
from users import User


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


bigsec = Admin('Big', 'Sec', 1, 'can add post', 'can delete post', 'can ban user', 'can promote others')
bigsec.show_privileges()

ally_privileges = Privileges('can add post', 'can comment posts', 'can delete posts')
ally = Admin('Ally', 'Sec', 3, ally_privileges)
print(f'The admin {ally.full_name()} has the following privileges :-')
ally_privileges.desc_privileges()
