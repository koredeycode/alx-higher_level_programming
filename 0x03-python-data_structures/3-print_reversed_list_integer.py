#!/usr/bin/python3
'''
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in my_list:
        print(i)'''
def print_reversed_list_integer(my_list=[]):
    l = len(my_list) - 1
    for i in range(l, -1, -1):
        print(my_list[i])
