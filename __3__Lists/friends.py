#3.1
#friends name
friends = ["vasanth","madha","kalai","ram","tejas"]
print(f"My friends are : \n{friends[0]}\n{friends[1]}\n{friends[2]}\n{friends[3]}\n{friends[4]}")

#3.2
#Private message
print(f"Hello {friends[0]}")
print(f"Welcome {friends[1]}")
print(f"Machi {friends[4]}")

#3.2
#Printing same message to everyone using for
for friend in friends:
	print(f"Hello {friend}")

#3.3
#cars
cars = ["bmw","jaguar","audi","benz","innova"]
car_favourite = f"My favourite car is {cars[1].title()}"
print(car_favourite)

#friends name in title
for friend in friends:
	friend_titles = friend.title()
	print(friend.title())

#storing everybody's title in a list
friends_titles = []
for friend in friends:
	apex = friend.title()
	friends_titles.append(apex)
print(friends_titles)

