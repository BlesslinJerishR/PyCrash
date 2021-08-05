from survey import AnonymousSurvey

# question
question = 'What language do you love the most ? '
my_survey = AnonymousSurvey(question)

# Show question and responses
my_survey.show_question()
print("Enter 'q' to quit \n")
while True:
    response = input('Language : ')
    if response == 'q':
        break
    my_survey.store_response(response)

# results
print('\nThanks for participating in the survey')
my_survey.show_results()
