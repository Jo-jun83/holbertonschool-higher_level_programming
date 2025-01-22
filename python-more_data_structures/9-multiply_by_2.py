#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Multiply each value in the dictionary by 2.

    Args:
        a_dictionary (dict): A dictionary with values to be multiplied.

    Returns:
        dict: A new dictionary with the same keys as `a_dictionary` and values
            that are each multiplied by 2.
    """
    new_dictionary = {}
    for i in a_dictionary:
        new_dictionary[i] = a_dictionary[i] * 2
    return new_dictionary
