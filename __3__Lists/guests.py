#3.4
guests = []
guests = ["rock","jill","rose","robert","paul"]
for guest in guests:
	print(f"{guest.title()} welcome to dinner")

#3.5
print(f"looks like {guests[4]} can't make it to the dinner")
guests.pop()
guest_new = "sheela"
guests.insert(4,guest_new)
print(f"welcome {guest_new.title()}")

for guest in guests:
	print(f"{guest.title()} Hope you will be present in the function please welcome")

#3.6
print("Guys I have found a big set of tables")
guest_0 = "avinash"
guest_3 = "abi"
guest_9 = "bava"
guests.insert(0,guest_0)
guests.insert(3,guest_3)
guests.append(guest_9)
for guest in guests:
	print(f"{guest.title()} Please welcome to the huge party")

#list titles
guest_titles = []
for guest in guests:
	apex = guest.title()
	guest_titles.append(apex)
#final lists
print(guests)
print(guest_titles)

#3.7
print("Sorry to inform you that we ran out of tables , so there is space for only two people")
for guest in range(6):
	removed_guest = guests.pop()
	print(f"{removed_guest.title()} sorry to inform you that we ran out of space")
print(guests)
for guest in guests:
	print(f"{guest.title()} you are still invited")
print(f"There are a total of {len(guests)} guests invited to the dinner, Finally.")

#del
#del guests[0]
#del guests[0]
for x in range(2):
	del guests[0]
print(guests)