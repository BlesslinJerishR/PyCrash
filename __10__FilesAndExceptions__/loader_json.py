import json
file = 'numbers.json'
with open(file, 'r') as jr:
    numbers = json.load(jr)
print(numbers)