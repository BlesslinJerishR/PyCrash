# movie_tickets.py
# 7.5
age = input("What is your age ? ")
age = int(age)
if age > 0:
    if age <= 3:
        print("Hurray, Ticket is free for you")
    elif age > 3 and age <= 12:
        print("Your Ticket cost is 10$ USD")
    elif age > 12:
        print("Your Ticket cost is 15$ USD")
else:
    print("You are a alien")