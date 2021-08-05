# cities_break.py

prompt = "Enter the place you have visited : "
while True:
    city = input(prompt)
    if city == "quit":
        break
    else:
        print(f"{city.title()}, nice place I would like to visit")
        print("Enter 'quit' once you have finished")