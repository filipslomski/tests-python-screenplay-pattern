from elements.baseElement import BaseElement


class Element(BaseElement):

    def __init__(self, locator, selector, context):
        super(Element, self).__init__(locator, selector, context)