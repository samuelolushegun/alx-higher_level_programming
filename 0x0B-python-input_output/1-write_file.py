#!/usr/bin/python3
'''Module write to a file'''


def write_file(filename="", text=""):
    '''
    This function writes a string to a text file (UTF8)
    and returns the number of characters written
    '''
    with open(filename, mode="w", encoding="utf") as my_fi:
        nb_ch_w = my_fi.write(text)
        return (nb_ch_w)
