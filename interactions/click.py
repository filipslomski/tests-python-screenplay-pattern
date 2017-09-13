from interactions.interaction import Interaction


class Click(Interaction):

    def __init__(self, context):
        self.element = None
        self.page = None
        super().__init__(context)

    def element(self, element):
        self.element = element
        return self
