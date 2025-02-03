#!/usr/bin/python3
"""This module defines a base class for a square."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class used to represent a Square, which is a subclass of Rectangle.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.
        """
        result = self.__size * self.__size
        return result

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        """
        return str("[Square] {}/{}".format(self.__size, self.__size))
