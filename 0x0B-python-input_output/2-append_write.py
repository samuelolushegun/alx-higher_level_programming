#!/usr/bin/python3
'''Module for appending to a file'''


def append_write(filename="", text=""):
    '''
    This function appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    '''
    with open(filename, mode="a", encoding="utf-8") as filou:
        return (filou.write(text))
