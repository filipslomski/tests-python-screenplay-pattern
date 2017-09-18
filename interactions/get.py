from interactions.interaction import Interaction


class Get(Interaction):

    def __init__(self, context):
        self.element = None
        self.attribute = None
        self.text = False
        super().__init__(context)

    def from_element(self, name):
        self.element = name

        return self

    def attribute(self, attr_name):
        self.attribute = attr_name

        return self

    def text(self):
        self.text = True

        return self

    def execute(self):
        return self.element.text if self.text else self.element.get_attribute(self.attribute)
