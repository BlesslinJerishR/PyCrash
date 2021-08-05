responses = {}
# poll
poll = True
while poll:
    name = input('What is your name ? ')
    actor = input('Who is your favourite actor ? ')
    responses[name] = actor
    person = input("Is there any other person who is willing to take the poll ?\nReply with 'yes' or 'no' \n")
    if person == 'no':
        poll = False
# poll is complete
print("People participated in the polls :-")
for name, actor in responses.items():
    print(f"{name}'s favourite actor is {actor}")
# print(responses)

