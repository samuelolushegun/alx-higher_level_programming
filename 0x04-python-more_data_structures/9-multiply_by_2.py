#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dictionary = dict()
    for key in a_dictionary:
        n_dictionary[key] = (a_dictionary[key] * 2)
    return n_dictionary
