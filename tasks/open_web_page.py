from tasks.task import Task
from interactions.open import Open


class Open_web_page(Task):

    def __init__(self, context):
        self.page_name = None
        self.context = context

    def with_name(self, page_name):
        self.page_name = page_name

    def perform_as(self, actor):

        return actor.attempts_to(
            Open(self.context).page(self.page_name)
        )
