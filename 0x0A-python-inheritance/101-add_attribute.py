#!/usr/bin/python3
"""This module contain the add_attribute function"""


def add_attribute(obj, attr, value):
    """Adds a new attribue if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
