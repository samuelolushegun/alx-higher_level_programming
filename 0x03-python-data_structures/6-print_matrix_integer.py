#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None or matrix == [[]]:
        print()
    else:
        for liste in matrix:
            idx_elmt = len(liste)
            for i in range(0, idx_elmt):
                print("{:d}".format(liste[i]), end="")
                if i != idx_elmt - 1:
                    print(" ", end="")
                else:
                    print()
