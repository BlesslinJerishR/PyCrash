# restaurant.py
# 7.2

seats = input("How many people are in your dinner menu ? ")
seats = int(seats)
if seats > 8:
    print("You need to wait for the table")
else:
    print("Your table is ready")