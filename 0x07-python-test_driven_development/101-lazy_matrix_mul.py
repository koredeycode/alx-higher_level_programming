#!/usr/bin/python3

"""This module contain a function that multiplies 2 matrices using
the numpy module"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Computes the multiplication of two matrices using the numpy module

    Arguments:
        m_a: the first matrix
        m_b: the second matrix
    Returns:
        the product of the matrices
    """
    return (np.matmul(m_a, m_b))
