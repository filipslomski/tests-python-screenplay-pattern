from interactions.interaction import Interaction


class Fill(Interaction):

    def __init__(self, context):
        self.value_to_fill = None
        self.field = None
        super().__init__(context)

    def value(self, value):
        self.value_to_fill = value

        return self

    def into_field(self, field):
        self.field = field

        return self
