#!/usr/bin/python3
def uppercase(str):
    str = str + "\n"
    for char in str:
        if ord(char) > 96 and ord(char) < 123:
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print(char, end="")
