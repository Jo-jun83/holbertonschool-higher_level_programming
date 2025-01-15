#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
res = abs(number) % 10
if number < 0:
    res = -res

if res > 5:
    text = "and is greater than 5"
elif res == 0:
    text = "and is 0"
elif res < 6:
    text = "and is less than 6 and not 0"
print("Last digit of {} is {} {:s}".format(number, res, text))
