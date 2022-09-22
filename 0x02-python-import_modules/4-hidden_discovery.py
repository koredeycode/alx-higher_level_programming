#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    hidlist = dir(hidden_4)
    for i in range(0, len(hidlist)):
        if hidlist[i][:2] == '__':
            continue
        print(hidlist[i])
