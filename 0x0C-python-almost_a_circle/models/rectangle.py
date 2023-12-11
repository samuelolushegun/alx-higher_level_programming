#!/usr/bin/python3
'''Module for rectangle class'''

from models.base import Base


class Rectangle(Base):
    '''Definition of rectangle class that is child of our base class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif (width <= 0):
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif (height <= 0):
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif (x < 0):
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif (y < 0):
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, largeur):
        if not isinstance(largeur, int):
            raise TypeError("width must be an integer")
        elif (largeur <= 0):
            raise ValueError("width must be > 0")
        self.__width = largeur

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, longueur):
        if not isinstance(longueur, int):
            raise TypeError("height must be an integer")
        elif (longueur <= 0):
            raise ValueError("height must be > 0")
        self.__height = longueur

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, abscisse):
        if not isinstance(abscisse, int):
            raise TypeError("x must be an integer")
        elif (abscisse < 0):
            raise ValueError("x must be >= 0")
        self.__x = abscisse

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, ordonne):
        if not isinstance(ordonne, int):
            raise TypeError("y must be an integer")
        elif (ordonne < 0):
            raise ValueError("y must be >= 0")
        self.__y = ordonne

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}" +
                f" - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        count = 1
        for arg in args:
            if count == 1:
                self.id = arg
            if count == 2:
                self.__width = arg
            if count == 3:
                self.__height = arg
            if count == 4:
                self.__x = arg
            if count == 5:
                self.__y = arg
            count += 1
        if count == 1:
            for key, value in kwargs.items():
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value
                if key == 'id':
                    self.id = value
