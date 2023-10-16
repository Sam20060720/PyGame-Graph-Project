from mylocals import *
from Drawable import Drawable
import pygame


class Text(Drawable):
    def __init__(self, position=(0, 0), text='', size=20, color=BLACK):
        super().__init__(position)
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont("Consolas", size)
        self.info = None
        self.set_text(text)

    def __repr__(self):
        return f"Text<{self.text}>"

    def draw(self, surface):
        surface.blit(self.info, (self.position[0] - self.info.get_width(
        ) / 2, self.position[1] - self.info.get_height() / 2))

    def set_text(self, text=''):
        self.info = self.font.render(self.text, True, self.color)
        self.text = text

    def get_text(self):
        return self.text

    def set_position(self, position):
        return super().set_position(position)
