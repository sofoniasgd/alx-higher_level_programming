#!/usr/bin/python3
"""A matrix division function module."""


def matrix_divided(matrix, div):
    """This functioun divides matrix with div.

    Args:
    matrix (list): the matrix in list type
    div (int or float): number that divides matrix

    Raises:
        TypeError: if matrix is not reactangular(same sized rows)
        and not a one dimentional list
        or it contains elements that are not int or float
        or div is not a number(int or float)
        ZeroDivisionError: if div is zero
    Returns:
        a new matrix whose each element is matrix/div
        for every element of original matrix
    """

    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    error2 = "Each row of the matrix must have the same size"
    # Check if matrix is n x n matrix(is one dimentional)
    if isinstance(matrix, list) and not isinstance(matrix[0], list):
        raise TypeError(error1)
    # Check if each element is int or float and each row is same width
    width = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != width:
            raise TypeError(error2)
        for j in range(len(matrix[i])):
            isint = isinstance(matrix[i][j], int)
            isfloat = isinstance(matrix[i][j], float)
            if not (isint or isfloat):
                raise TypeError(error1)
    # Check div if its now int or float
    if not ((isinstance(div, int) or isinstance(div, float)) and div == div):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    # Create new matrix and populate it
    new_matrix = [[0 for i in range(width)] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(width):
            new_matrix[i][j] = round(matrix[i][j] / div, 2)
    return new_matrix
