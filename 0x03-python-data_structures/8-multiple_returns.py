#!/usr/bin/python3

def multiple_returns(sentence):
    a = len(sentence)
    if len(sentence) == 0:
        b = None
    else:
        b = sentence[0]
    tup = (a, b)
    return (tup)
