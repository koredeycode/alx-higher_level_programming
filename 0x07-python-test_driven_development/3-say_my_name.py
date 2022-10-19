#!/usr/bin/python3
"""
This module a function say_my_name
The function prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
        This function print the first and last name in a sentence
        Arguments:
            first_name (str): the first name
            last_name (str): the last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
