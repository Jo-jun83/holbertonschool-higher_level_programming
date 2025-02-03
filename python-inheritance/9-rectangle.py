#!/usr/bin/python3
"""This module defines a base class for a rectangle."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle (BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        result = self.__width * self.__height
        return result

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.
        """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
