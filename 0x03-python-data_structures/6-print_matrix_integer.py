#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for i in range(len(matrix)):
        j = 0
        while j < len(matrix[i]):
            print("{:d}".format(matrix[i][j]), end=" ")
            if j == len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]))
            j = j + 1
