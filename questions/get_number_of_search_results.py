from questions.question import Question
from interactions.get import Get
from selectors.googlePage import GooglePage


class GetNumberOfSearchResults(Question):

    def __init__(self, context):
        self.context = context
        super().__init__(context)

    def perform_as(self, actor):

        return actor.attempts_to(
            Get(self.context).text().from_element(GooglePage.logged_user_email_info)
        )