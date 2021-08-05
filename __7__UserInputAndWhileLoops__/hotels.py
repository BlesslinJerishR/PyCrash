# 7.8
orders = ['sambar vada',
          'idly',
          'pongal',
          'poori',
          'idiyappam']
# 7.9
# Sambar vada is out
print('Sorry, We ran out of sambar vada')
for num in range(3):
    orders.append('sambar vada')
# alas hotel has run out of sambar vada
while 'sambar vada' in orders:
    orders.remove('sambar vada')

print(f'Available orderds : {orders}')
finished_orders = []
# print(orders)
# print(finished_orders)
if __name__ == '__main__':
    while len(orders) != 0:
        for order in orders:
            print(f'Your dish {order} has been prepared')
            orders.remove(order)
            cooked_order = order
            finished_orders.append(cooked_order)
    print(f'Pending orders : {orders}')
    print(f'Finished orders : {finished_orders}')
