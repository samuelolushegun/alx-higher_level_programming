#!/usr/bin/python3
'''
Module for My list
'''


class MyList(list):
    ''' New Object Mylist that inherits from the built-in object list '''

    def print_sorted(self):
        ''' Public method thet print the sorted list '''
        print(sorted(self))
