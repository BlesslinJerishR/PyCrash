# 9.11
# importing

from user_privilege_admin import User, Privileges, Admin

patel = Admin('Ded', 'Sec', 4, 'can add post', 'can delete post', 'can kick members', 'can ban users')
patel.show_privileges()