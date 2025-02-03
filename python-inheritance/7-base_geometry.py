#!/usr/bin/python3
"""This module defines a base class for geometry objects."""


class BaseGeometry:
    """
    Base class for geometry-related operations.

    Methods
    -------
    area()
        Raises an Exception indicating that the method is not implemented.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises
        ------
        Exception
            If the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the provided value is an integer and greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
