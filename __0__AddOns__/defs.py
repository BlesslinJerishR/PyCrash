# defs.py

# importing
import random
import string

# converting list to Titles
# Temporary
def list_titles(list):
    words_titles = []
    for word in list:
        title = word.title()
        words_titles.append(title)
    list = words_titles
    return list
    pass


# replacing original list with titles
# Permenant
def list_titles_permanent(list):
    for index, word in enumerate(list):
        # print(f" {index} : {word} ")
        for index, word_title in enumerate(list_titles(list)):
            if word.title() == word_title:
                list[index] = word_title
    return list


# removing duplicates in list
def list_duplicate_remover(list_1, list_2):
    list_temp = list_1 + list_2
    list_3 = list(set(list_temp))
    list_without_duplicates = list_3
    return list_3
    pass


# clearing lists
def list_clear(list):
    list.clear()
    return list
    pass


# numbers
def list_numbers(num):
    list_number = list(range(num + 1))
    return list_number
    pass


# zero remover
def zero_remover(list):
    list.pop(0)
    return list
    pass


# return each element in for loop
###BUG###

# To merge two dictionaries
def dict_merge(dict_1, dict_2):
    dict_3 = dict_1 | dict_2
    return dict_3
    pass


# converting dict to Titles
# Temporary
def dict_titles(dict):
    dict_titles = {}
    for key, value in dict.items():
        dict_titles.update({key.title(): value.title()})
    dict = dict_titles
    return dict
    pass


# replacing original dict with Titles
# Permanent
def dict_titles_permanent(dict):
    dname = {}
    dname.update(dict_titles(dict))
    return dname
    pass


# list to str using repr
def list_to_str(list):
    list = ",".join(repr(num) for num in list)
    return list
    pass


# list to str using repr without comma
def list_to_str_no_comma(list):
    list = "".join(repr(num) for num in list)
    return list
    pass


# random names
def random_names(num):
    names = []
    names_file = open('../_0_AddOns/names.txt').read().split()
    random.shuffle(names_file)
    for name in range(num):
        names.append(names_file[name])
    return names
    pass


# random animals
def random_animals(num):
    animals = []
    animals_file = open('../_0_AddOns/animals.txt').read().split('\n')
    random.shuffle(animals_file)
    for animal in range(num):
        animals.append(animals_file[animal])
    while 'list' in animals:
        animals.remove('list')
    return animals
    pass


# repeat items
def repeat_items(list):
    list_repeated = list
    num = list_numbers(5)
    num = zero_remover(num)
    num = random.choice(num)
    for item in list:
        for num in range(1, num):
            list_repeated.append(item)
    random.shuffle(list_repeated)
    return list_repeated
    pass


# your name
def name():
    name = input('What is your name ? ')
    return name


# remove last comma
def comma_remover(list):
    for item in range(len(list) - 1):
        print(f'{list[item]}', end=", ")
    print(f'{list[-1]} .')
    pass


# Tick Symbol
def tick():
    symbol = '\u2713'
    return symbol


# Cross Symbol
def cross():
    symbol = 'x'
    return symbol


# To List alphabets - Lower
def list_alphabets(num):
    alpha = []
    letters_lower = string.ascii_lowercase
    for num in range(num):
        letter = random.choice(letters_lower)
        alpha.append(letter)
    return alpha
    pass


# To List alphabets - Upper
def list_alphabets_upper(num):
    alpha = []
    letters_upper = string.ascii_uppercase
    for num in range(num):
        letter = random.choice(letters_upper)
        alpha.append(letter)
    return alpha
    pass


# To read a file
def read_file(file):
    with open(file, 'r') as fr:
        name = fr.read()
        return name

# Testing

