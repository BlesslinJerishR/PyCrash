# pizza_toppings.py
# 7.4
# 7.6
# pizza dictionary

pizza = {
    'toppings': []
}
print("Enter the pizza topping you would like to add to the pizza ! \nEnter 'enough' once you finish ordering or Enter 'quit' to cancel the order")
TOPPING = True
n = 1
while TOPPING:
    topping = input(f"Topping {n} : ")
    n += 1
    if topping == 'quit':
        print("Please, Visit again")
        TOPPING = False
        break
    elif topping == "enough":
        print("You have ordered a pizza with toppings : ",end=" ")
        for topping in pizza['toppings']:
            print(f"{topping}",end=",")
        print("etc ..")
        TOPPING = False
        break
    elif topping != 'enough' or 'quit':
        pizza['toppings'].append(topping)
        print(f"Adding '{topping}' topping to the pizza")
