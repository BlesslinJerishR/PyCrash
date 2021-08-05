# 10.12
import json
file = 'favourite_numbers.json'
with open(file, 'r') as fr:
    num = json.load(fr)
print(f'I know what is your favourite number . It is {num}')