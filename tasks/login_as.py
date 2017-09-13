from tasks.task import Task
from interactions.click import Click
from interactions.fill import Fill
from pageObjects.googlePage import GooglePage


class LoginAs(Task):

    def __init__(self, context):
        self.context = context

    def perform_as(self, actor):
        return actor.attempts_to(
            Fill(self.context).value(actor.email).into_field(GooglePage.email_field),
            Fill(self.context).value(actor.password).into_field(GooglePage.password_field),
            Click(self.context).element(GooglePage.login_next_button)
        )

@when(u'I login as user {username}')
def step_impl(context, username):
    context.google_page.login_as(credentials[username][0], credentials[username][1])