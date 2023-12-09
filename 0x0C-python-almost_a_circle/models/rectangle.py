#!/usr/bin/python3
'''Module for rectangle class'''

from models.base import Base


class Rectangle(Base):
    '''Definition of rectangle class that is child of our base class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            return (self.__width)

        @width.setter
        def width(self, largeur):
            self.__width = largeur

        @property
        def height(self):
            return (self.__height)

        @height.setter
        def height(self, longueur):
            self.__height = longueur

        @property
        def x(self):
            return (self.__x)

        @x.setter
        def x(self, abscisse):
            self.__x = abscisse

        @property
        def y(self):
            return (self.__y)

        @y.setter
        def y(self, ordonnée):
            self.__y = ordonnée
