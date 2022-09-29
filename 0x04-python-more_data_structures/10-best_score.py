#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    m = 0
    for i in a_dictionary:
        if a_dictionary.get(i) > m:
            ret = i
            m = a_dictionary.get(i)
    return (ret)
