#!/usr/bin/python3
''' Module for saving Object to a file'''
import json


def save_to_json_file(my_obj, filename):
    '''It writes an Object to a text file, using a JSON representation:'''
    with open(filename, mode="w") as m_file:
        json.dump(my_obj, m_file)
