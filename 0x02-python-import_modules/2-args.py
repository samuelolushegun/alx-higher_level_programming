#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    taille = len(argv) - 1
    if taille == 1:
        print("1 argument:\n1: {}".format(argv[1]))
    elif taille == 0:
        print("0 arguments.")
    else:
        print(f"{taille} arguments:")
        for i in range(1, taille + 1):
            print("{}: {}".format(i, argv[i]))
