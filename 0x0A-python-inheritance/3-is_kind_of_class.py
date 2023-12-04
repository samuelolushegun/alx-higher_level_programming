#!/usr/bin/python3
''' Module for a function that test is an object is instance of another '''


def is_kind_of_class(obj, a_class):
    '''
    This function returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False
    '''
    return (isinstance(obj, a_class))
