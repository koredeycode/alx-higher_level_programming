#!/usr/bin/python3
import math


class MagicClass:

    def __init__(self, radius):
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius is not a number")
        self.__radius = radius

    def area(self):
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        return (math.pi * 2 * self.__radius)
