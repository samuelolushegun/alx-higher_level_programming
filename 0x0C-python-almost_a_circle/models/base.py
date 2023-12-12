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
        if list_objs is None or list_objs == []:
            content = []
        else:
            content = [cls.to_dictionary(obj) for obj in list_objs]
        cl_name = cls.__name__
        f_name = f"{cl_name}.json"

        with open(f_name, 'w') as my_file:
            my_file.write(cls.to_json_string(content))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return ([])
        else:
            return (json.loads(json_string))
