#!/usr/bin/python3
"""
Contain the function that divides all elements of a matrix.
Matrix must be a list of lists of integers or floats

"""


def matrix_divided(matrix, div):
    """
    divides all elements in a matrix
    Arguments:
        matrix (list): the matrix to be divided
        div (int, float): the divisor
        Return: a new matrix
    """
    types = [int, float]
    b = all([type(i) in types for row in matrix for i in row])
    if (type(matrix) != list) or not b:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if len(set([len(i) for i in matrix])) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in types:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    ret = []

    for row in matrix:
        ret.append([round(i / div, 2) for i in row])
    return (ret)
