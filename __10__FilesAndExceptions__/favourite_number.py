# 10.11
import json
num = input('What is your favourite number ? ')
file = 'favourite_numbers.json'
with open(file, 'w') as fw:
    json.dump(num, fw)
