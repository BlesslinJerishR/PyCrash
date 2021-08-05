# 10.8
# 10.9
def read_file(file):
    with open(file, 'r') as fr:
        line = fr.read()
        print(line)

files = ['cats.txt', 'dogs.txt', 'butterfly.txt']
try:
    for file in files:
        read_file(file)
except FileNotFoundError:
    # print('File Not Found')
    pass