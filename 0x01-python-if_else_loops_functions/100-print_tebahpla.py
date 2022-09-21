#!/usr/bin/python3
def foo(x):
    if x % 2 == 0:
        return (x)
    return(x - 32)
for i in range(122, 96, -1):
    '''
    if i % 2 == 0:
        print(chr(i), end="")
    else:
        print(chr(i - 32), end="")'''
    print("{}".format(chr(foo(i))), end="")
