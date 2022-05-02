
class HelloModel:
    def __init__(self, name):
        name = name if name is not None else "World"
        self.message = "Hello %s!" % (name)
