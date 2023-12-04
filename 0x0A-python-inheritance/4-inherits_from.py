#!/usr/bin/python3
'''
Module contain a function that check if an object is an instance of a suclasses
'''


def inherits_from(obj, a_class):
    '''
    This function returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class
    otherwise False.
    '''
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return (True)
    else:
        return (False)
