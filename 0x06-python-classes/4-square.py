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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Return the area of a Square.
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Return the size  Square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Change the size of a  Square.
        Args:
            value (int): the size of the squar.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
