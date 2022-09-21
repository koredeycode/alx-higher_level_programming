#!/usr/bin/python3
def remove_char_at(str, n):
    sttr = ""
    for i in range(0, len(str)):
        if i != n:
            sttr += str[i]
    return (sttr)
