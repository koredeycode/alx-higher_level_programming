#!/usr/bin/python3
"""This module contain the implementatio of a list inheritance"""


class MyList(list):
    """This class inherit from list"""
    def print_sorted(self):
        """This function print the list in sorted form
        Arguments:
            self: the class instance
        """
        li = self.copy()
        li.sort()
        print("[", end="")
        for i, v in enumerate(li):
            print(v, end="")
            if i != len(li) - 1:
                print(", ", end="")
        print("]")
