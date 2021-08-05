# 7.10
# importing
from _0_AddOns.defs import name
responses ={}
polling = True
while polling:
    names = name()
    country = input('Which country would you like to visit for a vacation? ')
    responses[names] = country
    person = input("Is there anyone else who would like to participate in the poll? \nReply with 'yes' or 'no'\n")
    if person == 'no':
        polling = False
see = input("Would you like to see the results ? Reply with 'yes' or 'no'\n")
if see == 'yes':
    for name, country in responses.items():
        print(f'{name} will visit the country {country} on vacation')
