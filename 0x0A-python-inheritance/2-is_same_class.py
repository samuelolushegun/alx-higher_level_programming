#!/usr/bin/python3
'''
Module of a function that check if an object is exactly an instance of another
'''


def is_same_class(obj, a_class):
    '''
    This function checks if the object is exactly an instance of the specified
    class
    '''
    return (type(obj) is a_class)
