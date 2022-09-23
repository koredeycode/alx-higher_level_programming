#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    b = my_list[0]
    for i in my_list:
        if i > b:
            b = i
    return (b)


'''
def max_integer(listt):
    listt.sort()
    listt.reverse()
    return (listt[0])'''
