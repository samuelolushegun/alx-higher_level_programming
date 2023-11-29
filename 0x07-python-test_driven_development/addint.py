#!/usr/bin/python3
"""
    This module contains a function that adds two integers and return the
    result of addition or raise an exception if this happens.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
