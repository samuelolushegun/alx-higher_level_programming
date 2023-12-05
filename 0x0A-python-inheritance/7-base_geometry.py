#!/usr/bin/python3
'''Geometry module'''


class BaseGeometry:
    '''My Objecct BaseGeometry'''

    def area(self):
        '''Method that raised an Exception for the moment'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Method that validates value'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
