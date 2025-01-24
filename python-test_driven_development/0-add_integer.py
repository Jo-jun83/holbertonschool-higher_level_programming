#!/usr/bin/python3

"""
This module add two numbers
and return the sum of a and b
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int, float): The first number to add. Must be an integer or float.
        b (int, float, optional): The second number to add. Must be an integer
        or float. Defaults to 98.

    Returns:
        int: The sum of the two numbers as an integer.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
