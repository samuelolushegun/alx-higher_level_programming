#!/usr/bin/python3
'''
This Mdule contain function that lookup element in a object
'''


def lookup(obj):
    '''
    function that return the list of available attributes and methods
    of an object
    '''
    return (dir(obj))
