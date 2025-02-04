#!/usr/bin/python3
"""
This module defines the VerboseList class, which extends
the built-in list class
to provide additional functionality with verbose output
for certain list operations.
"""


class VerboseList(list):
    """
    A subclass of the built-in list that provides verbose output for
    certain operations.
    """
    def append(self, item):
        """
        Appends an item to the list and prints a message indicating
        the item was added.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """
        Extend the list by appending elements from the iterable `x`.
        """
        super().extend(x)
        print("Extended the list with [{}] items.".format(len(x)))

    def remove(self, item):
        """
        Remove an item from the list and print a message.
        """
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        """
        Remove and return item at index (default last).
        """
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
