#3.8
#seeing the world

world = ["singapore","usa","russia","france","china","japan"]
print(f"Original : {world}")
print(f"Sorted : {sorted(world)}")
print(f"Sorted Reverse : {sorted(world,reverse=True)}")
print(f"Original : {world}")
world.reverse()
print(f"Reverse : {world}")
world.reverse()
print(f"Reverse again : {world}")

#BUG (Fixed)
#print(world.reverse()) >> none
#xx
world.reverse()
print(f"Reversed world Bug : {world}")
world.sort()
print(f"Permenant sort : {world}")
world.sort(reverse=True)
print(f"Reversed Permenant sort : {world}")

#3.9
#did combining