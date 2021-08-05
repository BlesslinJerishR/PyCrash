# 10.10

with open('dance_of_life.txt', 'r', encoding='utf-8') as fr:
    name = fr.read()
    # print(name)
    the = name.lower().count('the ')
    print(the)