#!/usr/bin/python3
"""this module contain the append write function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file and return
    the number of character written"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))
