# 8.13
def build_person(first_name, last_name, age=None, **user_info):
    """To build a person to a dictionary"""
    user_info['first name'] = first_name,
    user_info['last name' ] = last_name,
    user_info['age'] = age,
    return user_info


print(build_person('Blesslin', 'Jerish', 20, place='India', language='Tamil'))