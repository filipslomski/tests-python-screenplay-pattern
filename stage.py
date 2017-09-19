from actors.filip import Filip
from actors.karol import Karol


class Stage(object):

    def __init__(self):
        self.current_actor = None

    def call_to_stage_for(self, actor):
        if actor == 'Filip':
            self.current_actor = Filip
        if actor == 'Karol':
            self.current_actor = Karol

    def the_actor_in_the_spotlight(self):
        return self.current_actor
