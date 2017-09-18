from tasks.task import Task
from interactions.fill import Fill
from interactions.click import Click


class Search(Task):

    def __init__(self, context):
        self.search_phrase = None
        self.search_suggestion = None
        self.context = context

    def for_phrase(self, phrase):
        self.search_phrase = phrase

        return self

    def then_select_from_search_suggestion(self, phrase):
        self.search_suggestion = phrase

        return self

    def perform_as(self, actor):
        actions = (Fill(self.context).value(self.search_phrase).into_field(self.context.google_page.search_field),)
        if self.search_suggestion:
            actions = actions + (
                Click(self.context).element(
                    self.context.google_page.search_suggestion.set_parameters(self.search_suggestion)),)

        return actor.attempts_to(
            actions
        )
