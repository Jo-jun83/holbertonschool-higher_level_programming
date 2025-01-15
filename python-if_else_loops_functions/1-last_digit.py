#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
result = abs(number) % 10
if result > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, result))
elif result == 0:
    print("Last digit of {} is {} and is 0".format(number, result))
else:
    print("Last digit of {} is {} and is less than 6".format(number, result))
