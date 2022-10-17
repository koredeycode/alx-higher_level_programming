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

    def area(self):
        """return the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * (self.width + self.height))

    def __str__(self):
        """return the string representation of the rectangle.
        Using the character "#"
        """
        ret_str = ""
        for i in range(self.height):
            for j in range(self.width):
                ret_str += "#"
            ret_str += "\n"
        return (ret_str[:-1])

    def __repr__(self):
        """return the canonical string representation of the rectangle.
        """
        return ("Rectangle({}, {})".format(self.width, self.height))
