#!/usr/bin/python3

"""This module contains the implementation of matrix and contains
a function that compute the multiplication of two matrices
"""


def helper(li, mb):
    """Helper function to the matrix_mul function
        Arguments:
            li (list): the row multiplier
            mb (list):  the matrice to be multiplied with
        Returns:
            a list of the multiplied product
    """
    cp = list(zip(*mb))

    ret = []
    for a in cp:
        s = 0
        for i in range(len(li)):
            s += li[i] * a[i]
        ret.append(s)
    return (ret)


def matrix_mul(m_a, m_b):
    """
    Computes the product of two matrices

    Arguments:
        m_a (list of lists): the first matrix
        m_b (list of lists): the second matrix

    Returns:
        the resulting matrix as a list of lists
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if not all(type(row) == list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(row) == list for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or not all([len(row) != 0 for row in m_a]):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or not all([len(row) != 0 for row in m_b]):
        raise ValueError("m_b can't be empty")
    types = [int, float]
    if not all([type(n) in types for row in m_a for n in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all([type(n) in types for row in m_b for n in row]):
        raise TypeError("m_b should contain only integers or floats")
    if len(set([len(row) for row in m_a])) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set([len(row) for row in m_b])) != 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    lst = []
    for li in m_a:
        lst.append(helper(li, m_b))
    return (lst)
