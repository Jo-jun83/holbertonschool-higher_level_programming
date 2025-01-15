#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
result = abs(num) % 10
if num < 0:
    result = -result

if result > 5:
    print("Last digit of {} is {} and is greater than 5".format(num, result))
elif result == 0:
    print("Last digit of {} is {} and is 0".format(num, result))
else:
    print("Last digit of {} is {} and is less than 6".format(num, result))
