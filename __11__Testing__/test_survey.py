import unittest
from survey import AnonymousSurvey
from anonymous_survey import question


class TestAnonymousSurvey(unittest.TestCase):
    """Test for class anonymously"""

    def test_unique_response(self):
        """To test unique responses"""
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_three_responses(self):
        """Test three responses"""
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Python']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()
