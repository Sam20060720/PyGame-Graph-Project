import abc

class Drawable(metaclass=abc.ABCMeta):
    def __init__(self, position=(0, 0)):
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    @abc.abstractmethod
    def draw(self, surface):
        pass