#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary with keys in sorted order.

    Args:
        a_dictionary (dict): The dictionary to be printed.

    Returns:
        None
    """
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
