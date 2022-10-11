#!/usr/bin/python3

"""This module contains class Named Square.
It get instantiated with size"""


class Square:
    """This class does nothing.
    Attributes:
        __size: size of the square
    """
    def __init__(self, size=0):
        """ Initialize a new Square.
        Args:
            size (int): the size of the squar.
        """
        if not type(size) == type(1):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
