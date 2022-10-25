#!/usr/bin/python3
"""This module contains a fuction for printing file content"""


def read_file(filename=""):
    """Prints the contenf of a text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
