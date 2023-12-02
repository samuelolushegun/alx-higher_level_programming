#!/usr/bin/python3
'''
This module is for divided matrix function
'''


def matrix_divided(matrix, div):
    '''
    divide each element for a matrix by argument div
    '''

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(matrix, list):
        new_mat = []
        for i in matrix:
            if isinstance(i, list):
                a = len(matrix[0])
                if len(i) == a:
                    nlist = []
                    for j in i:
                        if isinstance(j, (int, float)):
                            nlist.append(round((j / div), 2))
                        else:
                            raise TypeError("matrix must be a matrix (array "
                                            "of arrays of integers/floats)")
                    new_mat.append(nlist)
                else:
                    raise TypeError("Each row of the matrix must have the "
                                    "same size")
            else:
                raise TypeError("matrix must be a matrix (list of lists) of"
                                "integers/floats")
    else:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    return (new_mat)
