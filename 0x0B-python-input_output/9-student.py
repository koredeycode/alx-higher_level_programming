#!/usr/bin/python3
"""This module contain the class Student"""


class Student:
    """Defines the class student"""
    def __init__(self, first_name, last_name, age):
        """The initialization function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves the dictionary representation of a student"""
        return (self.__dict__)
