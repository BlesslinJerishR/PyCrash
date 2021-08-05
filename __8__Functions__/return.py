# return
def full_name_title(first_name, last_name):
    return f"{first_name.title()} {last_name.title()}"


name = full_name_title('blesslin', 'jerish')
print(name)


def full_name_title(first_name, last_name, middle_name=''):
    if middle_name:
        return f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        return f"{first_name.title()} {last_name.title()}"


name = full_name_title('chelliah', 'mani', 'retna')
print(name)
name = full_name_title('chelliah', 'retnamony')
print(name)

