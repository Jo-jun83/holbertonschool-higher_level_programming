#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Finds the maximum integer in a list.

    Args:
        my_list (list): A list of integers. Defaults to an empty list.

    Returns:
        int: The maximum integer in the list. If the list is empty,
        returns None.
    """
    if len(my_list) == 0:
        return None
    max_num = my_list[0]
    for i in my_list:
        if i > max_num:
            max_num = i
    return max_num
