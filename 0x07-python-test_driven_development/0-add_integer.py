#!/usr/bin/python3
"""
This module contains a function that adds two integers.
Check if the two numbers are of two types:
    float and
    integer.
    Raise TypeError when it failed to meet the condition
"""


def add_integer(a, b=98):
    """Add two integers and return the result
    Args:
        a (int): First integer
        b (int): Second integer
        Return: the result of a + b
    """
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
