class AnonymousSurvey:
    """Collects anonymous answers to survey questions"""

    def __init__(self, question):
        """Question & response storage """
        self.question = question
        self.responses = []

    def show_question(self):
        """question"""
        print(self.question)

    def store_response(self, new_response):
        """single response"""
        self.responses.append(new_response)

    def show_results(self):
        """Show responses"""
        print("Survey results: ")
        for response in self.responses:
            print(f' - {response}')


