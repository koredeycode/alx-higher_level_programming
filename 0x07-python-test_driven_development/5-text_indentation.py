#!/usr/bin/python3

"""This module contain a function that prints a
text with 2 new lines after each of these characters:
    ".", "?" and ":"
"""


def text_indentation(text):
    """This function prints a text with 2 new lines after each of these
    characters ., ? and :
    Arguments:
        text (str): the text to be printed
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    sym = [":", ".", "?"]
    for i, v in enumerate(text):
        if v == " " and text[i - 1] in sym:
            continue
        print(v, end="")
        if v in sym:
            print("\n")
