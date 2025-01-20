#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Determine which elements of a list are divisible by 2.

    Args:
        my_list (list): A list of integers.

    Returns:
        list: A list of boolean values where each boolean
        corresponds to whether the element at the same
        index in the input list is divisible by 2.
    """
    result = []
    for i in my_list:
        result.append(i % 2 == 0)
    return result
