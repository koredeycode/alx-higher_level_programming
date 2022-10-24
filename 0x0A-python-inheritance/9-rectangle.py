#!/usr/bin/python3
"""This module defines a class Rectangle inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The class Rectangle inheriting from BaseGeometry"""
    def __init__(self, width, height):
        """Initializer function"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the object"""
        return (self.__width * self.__height)

    def __str__(self):
        """Return a string representation of the object"""
        return ("[{}] {}/{}".format(self.__class__.__name__,
                                    self.__width, self.__height))
