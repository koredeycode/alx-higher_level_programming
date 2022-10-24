#!/usr/bin/python3


"""This module contain the lookup function"""


def lookup(obj):
    """this function returns the list of available attributes and methods
    of an object:
    Arguments:
        obj: the object
    Returns: the attributes and methods of an object
    """
    return (dir(obj))
