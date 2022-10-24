#!/usr/bin/python3
"""This module contains the function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is a class of a_class"""
    if type(obj) == a_class or isinstance(obj, a_class):
        return (True)
    return (False)
    """return (all([type(obj) == a_class, isinstance(obj, a_class)]))"""
