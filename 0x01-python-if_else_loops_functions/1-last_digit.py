#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    i = int(repr(number)[-1])
else:
    i = -int(repr(number)[-1])
if i == 0:
    print("Last digit of", number, "is", i, "and is 0")
elif i < 6 and i != 0:
    print("Last digit of", number, "is", i, "and is less than 6 and not 0")
else:
    print("Last digit of", number, "is", i, "and is greater than 5")
