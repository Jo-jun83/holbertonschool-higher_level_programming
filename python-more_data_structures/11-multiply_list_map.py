#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    Multiplies each element of a list by a given number using the map function.

    Args:
        my_list (list): The list of integers to be multiplied.
        number (int): The number by which each element of the list
        will be multiplied.

    Returns:
        list: A new list with each element multiplied by the given number.
    """
    res = list(map(lambda x: x * number, my_list))
    return res
