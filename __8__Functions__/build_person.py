# person dictionary
def build_person(first_name, last_name, age=None):
    """To build a person to a dictionary"""
    person = {
        'first name': first_name,
        'last name': last_name,
        'age': age,
    }
    return person


person = build_person('Blesslin', 'Jerish', '20')
print(person)
