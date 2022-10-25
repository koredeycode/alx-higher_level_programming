#!/usr/bin/python3
"""this module is a scripts that reads stdin line by line
and computes the metrics"""


def print_stats(size, stat):
    """Print the stats infos"""
    print("File size: {}".format(size))
    for k in sorted(stat):
        if stat[k] != 0:
            print("{}: {}".format(k, stat[k]))


with open(0, "r", encoding="utf-8") as std:
    fsize = 0
    dictt = {
                "200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "403": 0,
                "404": 0,
                "405": 0,
                "500": 0
            }
    count = 0
    try:
        for line in std:
            if count == 10:
                print_stats(fsize, dictt)
                count = 1
            else:
                count += 1
            li = line.split()
            try:
                fsize += int(li[-1])
            except (IndexError, ValueError):
                pass
            try:
                if li[-2] in dictt.keys():
                    if dictt.get(li[-2], -1) == -1:
                        dictt[li[-2]] = 1
                    else:
                        dictt[li[-2]] += 1
            except IndexError:
                pass
        print_stats(fsize, dictt)
    except KeyboardInterrupt:
        print_stats(fsize, dictt)
        raise
