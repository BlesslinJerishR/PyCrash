with open('pi.txt') as pi_txt:
    lines = pi_txt.readlines()
    for line in lines:
        print(line)

print()
pi_string = ""
for line in lines:
    pi_string += line.strip()
print(f'The value of pi is : {pi_string}')
print(f'Length of pi : {len(pi_string)}')



