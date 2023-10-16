from mylocals import *
import pygame
from pygame import gfxdraw
from Text import Text
from Vertex import Vertex


class Edge():
    def __init__(self, vertex1='', vertex2='', point1=(0, 0), point2=(0, 0), weight=0, color=BLACK, fontcolor=BLUE):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.point1 = point1
        self.point2 = point2
        self.weight = weight
        self.color = color
        self.caption = Text((0, 0), str(weight), 20, fontcolor)
        self.hidden = False

    def __repr__(self):
        return f'{self.get_names()[0]} - {self.get_names()[1]}'

    def __str__(self):
        return f'Edge<({self.get_names()[0]}-{self.get_names()[1]}:{self.weight})>'

    def draw(self, surface):
        if not self.hidden:
            gfxdraw.line(surface, self.point1[0], self.point1[1], self.point2[0],
                         self.point2[1], self.color)

            if self.point1[0] == self.point2[0]:
                self.caption.set_position(
                    ((self.point1[0] + self.point2[0])/2 + 14, (self.point1[1] + self.point2[1])/2))
                self.caption.draw(surface)
            else:
                self.caption.set_position(
                    ((self.point1[0] + self.point2[0])/2, (self.point1[1] + self.point2[1])/2 + 14))
                self.caption.draw(surface)

    def get_names(self):
        return self.vertex1.get_name(), self.vertex2.get_name()

    def get_weight(self):
        return self.weight

    def get_raw(self):
        return f"{self.vertex1.get_name()} {self.vertex2.get_name()} {self.weight}"

    def get_destination(self):
        return self.vertex2

    def get_source(self):
        return self.vertex1

    def set_color(self, color):
        self.color = color

    def hide(self, hide=True):
        self.hidden = hide
