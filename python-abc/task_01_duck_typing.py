#!/usr/bin/python3
"""
This module defines an abstract base class `Shape`
and its concrete subclasses `Circle` and `Rectangle`.
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    An abstract base class used to represent a geometric shape.
    Methods
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    A class used to represent a Circle, inheriting from Shape.
    """
    def __init__(self, radius):
        """
        Initializes a new instance of the class with a specified radius.
        """
        self.radius = abs(radius)

    def area(self):
        """
        Calculate the area of the circle.
        """
        return math.pi * self.radius * self.radius

    def perimeter(self):
        """
        Calculate the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    A class used to represent a Rectangle, inheriting from Shape.
    """
    def __init__(self, width, height):
        """
        Initializes a new instance of the class with a specified width
        and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the Rectangle.
        """
        return (self.width + self.height) * 2


def shape_info(shape):
    print("Area : {} \nPerimeter: {}".format(shape.area(), shape.perimeter()))
