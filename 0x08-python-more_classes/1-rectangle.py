#!/usr/bin/python3

"""This module contain the class Rectangle that define a rectangle"""


class Rectangle:
    """This class define a Rectangle"""
    def __init__(self, width=0, height=0):
        """This function initialize an instance
            Arguments:
                width (int): the width of the rectangle
                height (int): the height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """this return the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """This function set the height of the rectangle
            Arguments:
                value (int): the height of the rectangle
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """this return the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """This function set the width of the rectangle
            Arguments:
                value (int): the width of the rectangle
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
