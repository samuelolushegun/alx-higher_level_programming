#!/usr/bin/python3
'''Module for read file with python'''


def read_file(filename=""):
    '''This function reads a text file (UTF8) and prints it to stdout '''
    with open(filename, encoding="utf-8") as m_file:
        print(m_file.read(), end="")
