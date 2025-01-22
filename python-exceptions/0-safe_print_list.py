#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Prints up to x elements of a list safely.

    Args:
        my_list (list): The list to print elements from.
        Defaults to an empty list.
        x (int): The number of elements to print. Defaults to 0.

    Returns:
        int: The number of elements actually printed.
    """
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return x
    except Exception:
        print()
        return i
