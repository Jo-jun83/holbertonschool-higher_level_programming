#!/usr/bin/python3

def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        bool: True if value has been correctly printed
        (it means value is an integer), otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        if not isinstance(value, int):
            return False
