#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return (0)
    m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    li = list(m)
    for i in roman_string:
        if i not in li:
            return (0)
    ret = 0
    stack = list(roman_string)
    stack.reverse()
    while len(stack) != 0:
        a = stack.pop()
        if len(stack) != 0:
            b = stack.pop()
        else:
            ret += m.get(a)
            break
        if m.get(a) > m.get(b):
            ret += m.get(a)
            stack.append(b)
        elif m.get(a) == m.get(b):
            ret += m.get(a) + m.get(b)
        elif m.get(a) < m.get(b):
            ret += m.get(b) - m.get(a)
    return (ret)
