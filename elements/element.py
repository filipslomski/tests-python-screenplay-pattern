from elements.baseElement import BaseElement


class Element(BaseElement):

    def __init__(self, locator, selector):
        super(Element, self).__init__(locator, selector)