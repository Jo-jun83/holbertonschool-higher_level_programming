#!/usr/bin/python3

"""
This module print a string "My name is <first name> <lastname>
"""

def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name (str): The first name to be printed.
        last_name (str, optional): The last name to be printed. Defaults to an empty string.
    """

    if type(first_name) not in [str]:
            raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
            raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
