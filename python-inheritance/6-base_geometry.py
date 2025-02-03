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
