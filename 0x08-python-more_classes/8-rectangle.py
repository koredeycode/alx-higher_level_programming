#!/usr/bin/python3

"""This module contain the class Rectangle that define a rectangle"""


class Rectangle:
    """This class define a Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This function initialize an instance
            Arguments:
                width (int): the width of the rectangle
                height (int): the height of the rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return ("")
        ret = []
        for i in range(self.height):
            for j in range(self.width):
                ret.append(str(self.print_symbol))
            if i != self.height - 1:
                ret.append("\n")
        return ("".join(ret))

    def __repr__(self):
        """return the canonical string representation of the rectangle.
        """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Print deleting message when a Rectangle instance is deleted
        It also decrement the number of instances of the Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area
            Arguments:
                rect_1 (Rectangle): rectangle one
                rect_2 (Rectangle): rectangle two
            Returns:
                the biggest rectangle or rect_1 if equals
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
