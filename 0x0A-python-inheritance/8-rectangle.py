#!/usr/bin/python3
'''Rectangle Module'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Object Rectangle that inherits from BaseGeometry'''
    def __init__(self, width, height):
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height
