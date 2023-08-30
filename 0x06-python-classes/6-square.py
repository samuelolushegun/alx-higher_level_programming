#!/usr/bin/python3
"""This module Write a class Square that defines a square"""


class Square:
    """Simple class of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.

        Arg:
            size (int): size of the square.
            position (tuple): position of the square
        """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Make getter for my square position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """setter for position.

        Arg:
            value (tuple): value to set size of the square.
        """

        if type(value) is tuple and len(value) == 2 and type(value[0]) is int:
            if isinstance(value[1], int) and value[0] >= 0 and value[1] >= 0:
                self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Compute the square

        Returns:
            int: current square area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ prints in stdout the square with the character #"""
        p_check1 = type(self.__position) is tuple and len(self.__position) == 2
        if p_check1:
            pos_check_2a = type(self.__position[0]) is int
            pos_check_2b = isinstance(self.__position[1], int)
            if pos_check_2a and pos_check_2b:
                po_check3 = self.__position[0] >= 0 and self.__position[1] >= 0
                if self.__size > 0 and po_check3:
                    for y in range(0, self.__position[1]):
                        print()
                    for a in range(0, self.__size):
                        for x in range(0, self.__position[0]):
                            print(" ", end="")
                        for b in range(0, self.__size):
                            print("#", end="")
                        print()
                elif self.__size == 0:
                    print()
