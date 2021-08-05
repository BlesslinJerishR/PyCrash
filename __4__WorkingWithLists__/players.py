#slicing
players_list = ["sachin","dhoni","virat","watson","du plesis","natu"]
if __name__ == '__main__':
	players_list = ["sachin","dhoni","virat","watson","du plesis","natu"]
	print(players_list)
	print(players_list[0:1])
	print(players_list[:3])
	print(players_list[1:5])
	print(players_list[-2:])
	
	#for loop using slices
	for player in players_list[-3:]:
		print(player.title())
	
	#copying a list using slices
	players_list = ["sachin","dhoni","virat","watson","du plesis","natu"]
	players_friends = players_list[:]
	print(f"My favourite players are : {players_list}")
	print(f"My friend's favourite players are : {players_friends}")
	
	#using for loop without list bracket
	print("Players without bracket from lists :- ")
	print(f"My favourite players are : ",end=" ")
	for player in players_list:
		print(player, end=", ")
