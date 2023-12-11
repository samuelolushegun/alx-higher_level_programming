#!/usr/bin/python3
'''Module for Base class'''
import json


class Base:
    '''
    Base class will be the “base” of all other classes in this project
    It will manage id attribute in all futures classes
    and to avoid duplicating the same code
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            content = []
        else:
            content = Base.to_json_string(list_objs)
        if type(list_objs[0]) is Square:
            f_name = 'Square.json'
        elif type(list_objs[0]) is Rectangle:
            f_name = 'Rectangle.json'
        with open(f_name, 'w') as my_file:
            my_file.write(content)
