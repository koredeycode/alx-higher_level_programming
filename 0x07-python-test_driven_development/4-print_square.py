#!/usr/bin/python3
"""
    This module contain a function that prints a square with
    the character "#"
"""


def print_square(size):
    """
    Prints a square with the character "#" depending on size

    Arguments:
        size (int): the size of the square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
