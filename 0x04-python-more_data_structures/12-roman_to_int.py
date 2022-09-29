#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not roman_string.isalpha:
        return (0)
    m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    li = list(m)
    ret = 0
    for i in roman_string:
        if i not in li:
            return (0)

    i = 0
    lent = len(roman_string)

    while i < lent:
        a = li.index(roman_string[i])
        if i + 1 < lent:
            b = li.index(roman_string[i + 1])
        else:
            b = 0
        if a >= b:
            ret += m.get(li[a])
            i += 1
            continue
        elif a < b:
            ret += abs(m.get(li[b]) - m.get(li[a]))
            i += 2
            continue
    return (ret)
