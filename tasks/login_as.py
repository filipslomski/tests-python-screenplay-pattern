from tasks.task import Task
from interactions.click import Click
from interactions.fill import Fill


class LoginAs(Task):

    def __init__(self, context):
        self.context = context

    def perform_as(self, actor):

        return actor.attempts_to(
            Fill(self.context).value(actor.email).into_field(self.context.google_page.email_field),
            Fill(self.context).value(actor.password).into_field(self.context.google_page.password_field),
            Click(self.context).element(self.context.google_page.login_next_button)
        )
