#!/usr/bin/python3
"""this module contains the pascal triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    Pascal triangles of n"""
    ret = []
    if n <= 0:
        return (ret)
    ret.append([1])
    for i in range(n-1):
        lnt = len(ret[-1])
        tmp = [1]
        for idx, v in enumerate(ret[-1]):
            if idx != lnt - 1:
                tmp.append(v + ret[-1][idx + 1])
        tmp.append(1)
        ret.append(tmp)
    return (ret)
