#!/usr/bin/python3
"""
This module defines a class MyInt that inherits from the built-in int class.
"""


class MyInt(int):
    """
    MyInt is a subclass of int that inverts the behavior of == and != operators.
    """
    def __eq__(self, other):
        """
        Overrides the equality operator to invert its behavior.
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """
        Overrides the not equal operator to invert its behavior.
        """
        return not super().__ne__(other)
