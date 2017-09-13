class Actor(object):

    def __init__(self):
        pass

    def attempts_to(self, *args):
        for arg in args:
            arg.execute()