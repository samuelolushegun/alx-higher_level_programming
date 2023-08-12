#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    somme = 0
    if len(argv) > 1:
        for arg in range(1, len(argv)):
            somme = somme + int(argv[arg])
    print(somme)
