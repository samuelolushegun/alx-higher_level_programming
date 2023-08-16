#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    for List in matrix:
        n_List = []
        for e in List:
            n_List.append(e * e)
        n_matrix.append(n_List)
    return n_matrix
