#!/usr/bin/python3
"""The module contain the implementation of a class
inferred from a given bytecode"""
import math


class MagicClass:
    """Coding a class from a bytecode
    """
    def __init__(self, radius=0):
        """Initialization function"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the object"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Return the circumference of the object"""
        return (math.pi * 2 * self.__radius)
