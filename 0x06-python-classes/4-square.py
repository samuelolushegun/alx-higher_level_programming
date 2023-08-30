#!/usr/bin/python3
"""This module write an empty class Square that defines a square"""


class Square:
    """Simple class of a square"""

    def __init__(self, size=0):
        """Initialize the square.

        Arg:
            size (int): size of the square.
        """

        self.__size = size

    @property
    def size(self):
        """Make getter for my square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter for size.

        Arg:
            value (int): value to set size of the square.
        """

        if type(value) is int and value >= 0:
            self.__size = value
        elif type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Compute the square

        Returns:
            int: current square area
        """
        return (self.__size * self.__size)
