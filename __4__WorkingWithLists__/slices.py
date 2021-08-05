#4.10
from players import players_list
print(players_list)
print(f"The first three items in the list are : {players_list[0:3]}")
players_list.append("raina")
print(players_list)
print(f"The three items from the middle of the list are : {players_list[2:5]}")
print(f"The last three items in the list are : {players_list[-3:]}")

#4.11
from pizzas import pizzas
pizzas_friends = pizzas[:]
pizzas.append("onion")
print(pizzas)
pizzas_friends.append("double cheese")
print(pizzas_friends)

for pizza in pizzas:
	print(f"My favourite pizzas are : {pizza.title()}")

for pizza in pizzas_friends:
	print(f"My friend's favourite pizzas are : {pizza.title()}")

#4.12
pizzas_total = []
for pizza in pizzas:
	#print(f"{pizza.title()}")
	pizzas_total.append(pizza)
for pizza in pizzas_friends:
	#print(f"{pizza.title()}")
	pizzas_total.append(pizza)
print(f"The total pizzas are : {pizzas_total}")

#removing duplicates
legit_pizzas = []
for pizza in pizzas_total:
	if pizza not in legit_pizzas:
		legit_pizzas.append(pizza)
print(f"The real pizzas are : {legit_pizzas}")