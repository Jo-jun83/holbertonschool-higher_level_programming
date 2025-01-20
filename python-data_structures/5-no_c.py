#!/usr/bin/python3

def no_c(my_string):
    """
    Removes all characters 'c' and 'C' from the input string.

    Args:
        my_string (str): The input string from which 'c' and 'C'
        characters will be removed.

    Returns:
        str: A new string with all 'c' and 'C' characters removed.
    """
    new_string = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        new_string += i
    return new_string
