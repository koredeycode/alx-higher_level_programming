#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    ac = len(sys.argv)
    if ac < 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    operator = sys.argv[2]
    a, b = int(sys.argv[1]), int(sys.argv[3])
    if operator == '+':
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        sys.exit(0)
    if operator == '-':
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        sys.exit(0)
    if operator == '*':
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        sys.exit(0)
    if operator == '/':
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))
        sys.exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
