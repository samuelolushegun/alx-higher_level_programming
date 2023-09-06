#!/usr/bin/python3
"""
    My Rectangle Module
"""


class Rectangle:
    """This object defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) is int and value >= 0:
            self.__width = value
        elif type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) is int and value >= 0:
            self.__height = value
        elif type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            raise ValueError("height must be >= 0")
