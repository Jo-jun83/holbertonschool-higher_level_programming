#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print.

    Returns:
        int: The number of integers printed.

    Raises:
        TypeError: If an element in the list is not an integer.
        IndexError: If x is greater than the length of the list.
    """
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
            print()
            return x
    except IndexError:
        print()