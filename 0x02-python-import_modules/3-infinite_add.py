#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    ac = len(sys.argv)
    _sum = 0
    if ac > 1:
        for i in range(1, ac):
            _sum += int(sys.argv[i])
    print(_sum)
