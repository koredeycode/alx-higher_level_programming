#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    retlist = []
    for i in my_list:
        if i % 2 == 0:
            retlist.append(True)
        else:
            retlist.append(False)
    return (retlist)
