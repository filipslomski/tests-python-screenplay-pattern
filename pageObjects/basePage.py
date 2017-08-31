from stringConstants import Strings


class BasePage(object):

    def __init__(self, context):
        self.context = context
        self.URL = ""

    def open(self):
        self.context.driver.get(self.context.base_url + self.URL)

    string = Strings.EXAMPLE_STRING
