#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
lastdigit = abs(number) % 10
if number < 0:
    lastdigit = -lastdigit
print(f"Last digit of {number:d} is {lastdigit:d} ", end="")
if lastdigit > 5:
    print("and is greater 5")
elif lastdigit == 0:
    print("and is 0")
elif lastdigit < 6 and lastdigit != 0:
    print("and is less than 6 and not 0")
