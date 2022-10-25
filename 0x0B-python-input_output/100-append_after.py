#!/usr/bin/python3
"""this module contains the append after function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
    containing a specific string"""
    txt = ""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as f:
        f.write(txt)
