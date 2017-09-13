from interactions.interaction import Interaction


class Open(Interaction):

    def __init__(self, context):
        self.custom_url = None
        super().__init__(context)

    def custom_url(self, page_url):
        self.custom_url = page_url
        return self

    def page(self, page_name):
