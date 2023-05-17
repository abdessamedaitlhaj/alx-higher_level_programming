#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for l in matrix:
        new_matrix.append(list(map(lambda x: pow(x, 2), l)))
    return new_matrix
