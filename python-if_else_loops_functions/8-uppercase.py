#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            upper_char = chr(ord(i) - 32)
        else:
            upper_char = i
        print("{}".format(upper_char), end="")
    print()
