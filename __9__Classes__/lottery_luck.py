# 9.15
import lottery

# winning tickets
number_winner = 5362
letter_winner = 'gapp'

# my tickets
number_ticket = 7465
letter_ticket = 'igra'

tried = True
tries = 0
while tried:
    winner = lottery.number_selector()
    if int(winner) != number_ticket:
        tries += 1
        print(f"Lottery number : {winner}\n")
        print(f"Tries : {tries}")
    elif int(winner) == number_ticket:
        tries += 1
        print("Congrats, You are the winner")
        print(f'Your Ticket number is : {winner}')
        print(f'Total tries : {tries}')
        tried = False
        break
