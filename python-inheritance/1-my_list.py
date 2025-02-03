#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
"""


class MyList(list):
    """
    A subclass of the built-in list class that includes an additional
    method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
