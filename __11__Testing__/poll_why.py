# 10.5
responses = 'responses.txt'
with open(responses, 'a') as response:
    response.write('\nPoll Results and Reasons\n')
    poll = True
    person = 0
    while poll:
        name = input('\nWhat is your name : ')
        who = input('Who is your favourite actor ? ')
        why = input('Why is he your favourite actor ? ')
        person += 1
        response.write(f'Name : {name} \nFavourite actor : {who} \nReason : {why}\n')
        if person == 3:
            poll = False
