#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tx = tuple_a + (0, 0)
    ty = tuple_b + (0, 0)
    x = tx[0] + ty[0]
    y = tx[1] + ty[1]
    a = (x, y)
    return (a)
