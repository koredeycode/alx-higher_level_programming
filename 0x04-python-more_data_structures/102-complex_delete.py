#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lk = list(a_dictionary)
    lv = list(map(lambda x: a_dictionary.get(x), lk))

    for i in lv:
        if i == value:
            del a_dictionary[lk[lv.index(i)]]
    return (a_dictionary)
