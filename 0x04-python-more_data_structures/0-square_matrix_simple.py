#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(range(len(matrix)))
    for i in new_matrix:
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))
    return new_matrix
