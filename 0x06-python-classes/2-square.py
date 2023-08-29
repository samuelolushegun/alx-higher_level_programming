#!/usr/bin/python3
"""This module write an empty class Square that defines a square"""


class Square:
    """Simple class of a square"""

    def __init__(self, size=0):
        """Initialize the square.

        Arg:
            size (int): size of the square.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
