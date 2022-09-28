#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    li = sorted(list(a_dictionary))
    for i in li:
        print("{}: {}".format(i, a_dictionary[i]))
