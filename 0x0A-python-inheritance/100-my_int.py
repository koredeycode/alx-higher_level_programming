#!/usr/bin/python3
"""This module contain the rebellious MyInt class"""


class MyInt(int):
    """invert int operators == and !=."""
    def __eq__(self, other):
        """exchange == with !="""
        return (self.real != other)

    def __ne__(self, other):
        """exchange != with =="""
        return (self.real == other)
