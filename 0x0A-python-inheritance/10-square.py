#!/usr/bin/python3
'''Square Module'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Object Square that is child of Rectangle'''
    def __init__(self, size):
        super().integer_validator('size', size)
        super().__init__(size, size)

#    def area(self):
#        return (self.__size ** 2)
