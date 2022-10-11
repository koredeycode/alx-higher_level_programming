#!/usr/bin/python3

"""This module contains class Named Square.
It get instantiated with size"""


class Square:
    """This class does nothing.
    Attributes:
        __size: size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize a new Square.
        Args:
            size (int): the size of the squar.
            position (tuple): position
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        b1 = not all(isinstance(n, int) for n in position)
        if not b1:
            b2 = not all(n >= 0 for n in position)
        else:
            b2 = 0
        b3 = not isinstance(position, tuple)
        b4 = len(position) != 2
        if b1 or b2 or b3 or b4:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def position(self):
        """Return the square position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the square position"""
        b1 = not all(isinstance(n, int) for n in value)
        if not b1:
            b2 = not all(n >= 0 for n in value)
        else:
            b2 = 0
        b3 = not isinstance(value, tuple)
        b4 = len(value) != 2
        if b1 or b2 or b3 or b4:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
    def size(self, value=0):
        """ Change the size of a  Square.
        Args:
            value (int): the size of the squar.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """print the square"""
        if self.__size == 0:
            print()
            return
        for a in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for a in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
