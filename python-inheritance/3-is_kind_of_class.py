#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance
or an inherited instance of a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance or inherited instance
    of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        True if obj is an instance or inherited instance
        of a_class, otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
