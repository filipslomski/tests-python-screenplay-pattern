from elements.baseElement import BaseElement


class Checkbox(BaseElement):

    def __init__(self, locator, selector, context):
        super(Checkbox, self).__init__(locator, selector, context)

    def check(self):
        pass

    def uncheck(self):
        pass