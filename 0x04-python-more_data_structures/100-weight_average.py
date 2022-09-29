#!/usr/bin/python3
def weight_average(my_list=[]):
    s = 0
    f = 0
    if not my_list:
        return (0)
    for i in my_list:
        s += i[0] * i[1]
        f += i[1]
    return (s / f)
