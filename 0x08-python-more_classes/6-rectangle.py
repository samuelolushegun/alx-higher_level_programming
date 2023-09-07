#!/usr/bin/python3
"""
    My Rectangle Module
"""


class Rectangle:
    """This object defines a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width
        self.number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return ((self.__height + self.__width) * 2)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ("")
        else:
            for h in range(self.__height - 1):
                print("#" * self.width)
            print("#" * self.width, end="")
            return ("")

    def __repr__(self):
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        print("Bye rectangle...")
