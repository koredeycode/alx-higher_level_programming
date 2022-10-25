#!usr/bin/python3
"""This module contain the write file function"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns the number of 
    characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
