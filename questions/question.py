class Question(object):

    def __init__(self, context):
        self.page = None
        self.context = context

    def on_page(self, page_name):
        self.page = page_name