#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    This function takes a list of integers and prints them one by one.

    Args:
    my_list (list): A list of integers.

    Returns:
    None
    """
    for i in my_list:
        print("{:d}".format(i))
