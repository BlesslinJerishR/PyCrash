#alien_colors.py
#5.3
alien_color = "green"
if alien_color == "green":
	print("Congratulations, the player just earned 5 points")
	alien_shot = alien_color
	print(f"You have shot down {alien_shot} alien")

#5.4
alien_color ="yellow"
if alien_color == "green":
	points = 5
	print(f"Congratulations, the player just earned {points} points")
	alien_shot = alien_color
	print(f"You have shot down {alien_shot} alien")
else:
	points = 10
	print(f"Congratulations, the player just earned {points} points")
	alien_shot = alien_color
	print(f"You have shot down {alien_shot} alien")

#5.5
alien_color = "red"
if alien_color == "green":
	points = 5
	print(f"Congratulations, the player just earned {points} points")
	alien_shot = alien_color
	print(f"You have shot down {alien_shot} alien")	
elif alien_color == "yellow":
	points = 10
	print(f"Congratulations, the player just earned {points} points")
	alien_shot = alien_color
	print(f"You have shot down {alien_shot} alien")
elif alien_color == "red":
	points = 15
	print(f"Congratulations, the player just earned {points} points")
	alien_shot = alien_color
	print(f"You have shot down {alien_shot} alien")
