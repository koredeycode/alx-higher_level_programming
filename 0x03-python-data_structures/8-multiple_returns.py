#!/usr/bin/python3

def multiple_returns(sentence):
    a = len(sentence)
    b = sentence[0]
    if len(sentence) == 0:
        b = None
    tup = (a, b)
    return (tup)
