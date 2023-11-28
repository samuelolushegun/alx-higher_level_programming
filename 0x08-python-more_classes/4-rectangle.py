#!/usr/bin/python3
"""
This is a Rectangle module
"""


class Rectangle:
    """Object Rectangle that define a restangle"""
    def __init__(self, width=0, height=0):

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        return (self.__width)

    @property
    def height(self):
        return (self.__height)

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        if (self.__width == 0) or (self.__height == 0):
            return ("")
        else:
            for i in range(self.__height - 1):
                print("#" * self.__width)
            return ("#" * self.__width)

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")
