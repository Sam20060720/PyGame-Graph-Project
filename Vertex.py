from mylocals import *
from Drawable import Drawable
import pygame
from pygame import gfxdraw, font, rect
from Text import Text


class Vertex(Drawable):
    def __init__(self, position=(0, 0), name='', outer_color=V_OUTER, inner_color=V_INNER, radius=V_RADIUS):
        self.position = position
        self.name = name
        self.caption = Text(position, name, 20, BLACK)
        self.dist_text = ''
        self.dist = Text(
            (self.position[0], self.position[1]+16), self.dist_text, 18, GREEN)
        self.outer_color = outer_color
        self.inner_color = inner_color
        self.caption_color = BLACK

        self.V_RADIUS = radius

    def draw(self, surface):
        # 外面的圓
        gfxdraw.aacircle(
            surface, self.position[0], self.position[1], self.V_RADIUS, self.outer_color)  # 抗鋸齒的圆
        gfxdraw.filled_circle(
            surface, self.position[0], self.position[1], self.V_RADIUS, self.outer_color)
        # 裡面的圓
        gfxdraw.aacircle(
            surface, self.position[0], self.position[1], self.V_RADIUS-2, self.inner_color)
        gfxdraw.filled_circle(
            surface, self.position[0], self.position[1], self.V_RADIUS-2, self.inner_color)
        # 文字
        self.caption = Text(self.position, self.name, 20, self.caption_color)
        self.caption.draw(surface)
        self.dist.draw(surface)

    def __repr__(self) -> str:
        return f'Vertex<{self.name}>'

    def get_name(self):
        return self.name

    def set_caption_color(self, color=BLACK):
        self.caption_color = color

    def set_dist_text(self, surface, text=''):
        self.dist_text = str(text)
        self.dist.set_text(self.dist_text)

    def get_position(self):
        return self.position

    def get_weight(self):
        return 0
