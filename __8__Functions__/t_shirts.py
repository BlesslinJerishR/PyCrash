# 8.3
def make_shirt(size, message):
    """To get the shirt size and the message to print"""
    print(f'Your ordered shirt size is {size} embroidered with the message : {message}')


make_shirt('XL', 'No 7')
make_shirt(message='HipHop Tamizha', size='L')

# 8.4
def make_shirt(size='large', message='I love python'):
    print(f'Your ordered shirt size is {size} embroidered with the message : {message}')


make_shirt()
make_shirt(size='medium')
make_shirt(message='Python is awesome')
