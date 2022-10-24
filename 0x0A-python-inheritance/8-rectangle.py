#!/usr/bin/python3
"""This module defines a class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The class Rectangle inheriting from BaseGeometry"""
    def __init__(self, width, height):
        """The initializer function"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
