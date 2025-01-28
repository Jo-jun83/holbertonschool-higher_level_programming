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

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square. Must be an integer
            greater than or equal to 0.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Prints the square using the '#' character.

        The size of the square is determined by the private instance
        attribute __size.
        If __size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
