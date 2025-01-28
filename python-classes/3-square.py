#!/usr/bin/python3

"""This module defines a class Square"""


class Square:
    """this class define a square"""

    def __init__(self, size=0):
        """
        Initialize the square with a size
        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
