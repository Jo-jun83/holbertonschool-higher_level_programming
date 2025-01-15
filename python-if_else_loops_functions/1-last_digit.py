#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
res = abs(number) % 10
if number < 0:
    res = -res

if res > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, res))
elif res == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, res))
else:
    print("Last digit of {:d} is {:d} and is less than 6".format(number, res))
