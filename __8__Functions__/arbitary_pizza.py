def pizza_toppings(*toppings):
    """Enter the requested toppings"""
    for topping in toppings:
        print(f"Adding {topping} toppings to pizza")
    print(">>>Pizza Summary<<<")
    print("Making a pizza with these toppings")
    for topping in toppings:
        print(f"- {topping}")

pizza_toppings('honey', 'tomato', 'cheese')
