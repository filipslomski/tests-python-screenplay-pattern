from interactions.interaction import Interaction

class Open(Interaction):

    def __init__(self, context):
        self.context = context
        self.url = None
        super().__init__(context)

    def custom_url(self, page_url):
        self.url = page_url

        return self

    def page(self, page_name):
        self.url = self.context.page_name.URL

    def execute(self):
        self.context.browser.get(self.url)