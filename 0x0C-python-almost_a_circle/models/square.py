#!/usr/bin/python3
'''Sqaure's Module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''The Class Square whose is a particular rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Init method of cléss Square'''

        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        elif (size <= 0):
            raise ValueError("width must be > 0")
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.__width = size
        self.__height = size

    @property
    def size(self):
        '''getter for attribute size'''
        return (self.__width)

    @size.setter
    def size(self, cote):
        '''setter for size attribute'''
        if not isinstance(cote, int):
            raise TypeError("width must be an integer")
        elif (cote <= 0):
            raise ValueError("width must be > 0")
        self.__width = cote
        self.__height = cote

    def __str__(self):
        '''return a readable repr of square'''
        return (f"[square] ({self.id}) {self.x}/{self.y} - {self.__width}")

    def update(self, *args, **kwargs):
        '''methode to update squares attributes'''
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
                    self.__height = value
                    self.__width = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
                if key == 'id':
                    self.id = value

    def to_dictionary(self):
        '''methode to return et dict representaiont of the square'''
        sq_dict = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }
        return (sq_dict)
