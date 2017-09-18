from questions.question import Question
from interactions.get import Get
from interactions.click import Click
from selectors.googlePage import GooglePage


class GetLoggedUser(Question):

    def __init__(self, context):
        self.context = context
        super().__init__(context)

    def perform_as(self, actor):

        return actor.attempts_to(
            Click(self.context).element(GooglePage.logged_user_icon),
            Get(self.context).text().from_element(GooglePage.logged_user_email_info)
        )