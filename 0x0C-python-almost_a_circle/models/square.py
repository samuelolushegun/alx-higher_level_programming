#!/usr/bin/pyhton3
'''Sqaure's Module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''The Class Square whose is a particular rectangle'''

    def __init__(self, size, x=0, y=0, id=None):

        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        elif (size <= 0):
            raise ValueError("width must be > 0")
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.__width = size
        self.__height = size

    @property
    def size(self):
        return (self.__width)

    @size.setter
    def size(self, cote):
        if not isinstance(cote, int):
            raise TypeError("width must be an integer")
        elif (cote <= 0):
            raise ValueError("width must be > 0")
        self.__width = cote
        self.__height = cote

    def __str__(self):
        return (f"[square] ({self.id}) {self.x}/{self.y} - {self.__width}")

    def update(self, *args, **kwargs):
        count = 1
        for arg in args:
            if count == 1:
                self.id = arg
            if count == 2:
                self.size = arg
            if count == 3:
                self.x = arg
            if count == 4:
                self.y = arg
            count += 1
        if count == 1:
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
                if key == 'id':
                    self.id = value
