#!/usr/bin/python3
"""This module contain a function that checks the instance of the object"""


def is_same_class(obj, a_class):
    """This function check for the instance of the specified class
    Arguments:
        obj: object instance
        a_class: class to be compared with
    """
    return (type(obj) == a_class)
