#!/usr/bin/python3

"""This module defines a class Rectangle"""


class Rectangle:
    """this class define a rectangle"""
    def __init__(self, width=0, height=0, print_symbol="#"):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_1 if rect_1.area() > rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a new Rectangle instance with width and height equal to size.

        Args:
            size: The size of the rectangle's width and height. Defaults to 0.

        Returns:
            Rectangle: A new Rectangle instance with w and h set to size.
        """
        return cls(size, size)

    @property
    def width(self):
        """
        Getter method that retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width value to set.
            Must be an integer greater than or equal to 0.

        Raises:
            TypeError: If the provided width is not an integer.
            ValueError: If the provided width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The height value to set.
            Must be a non-negative integer.

        Raises:
            TypeError: If the provided height is not an integer.
            ValueError: If the provided height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle, calculated as
            width multiplied by height.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, which is the sum
            of twice the width and twice the height.
                  If either the width or height is zero, the perimeter
                  is considered to be zero.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            result = (self.__width + self.__height) * 2
            return result

    def __str__(self):
        """
        Returns a string representation of the rectangle
        using the `print_symbol`.
        If either the width or height of the rectangle is 0,
        returns an empty string.
        Otherwise, constructs a string where each line represents
        a row of the rectangle,
        with each row containing the `print_symbol` repeated `width`
        times, and the rows
        separated by newline characters.
        Returns:
            str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = [
                str(self.print_symbol) * self.__width
                for i in range(self.__height)
            ]
            return "\n".join(rectangle_str)

    def __repr__(self):
        """
        Return a string representation of the Rectangle instance
        that can be used to recreate
        the object. The string is formatted as 'Rectangle(width, height)'.

        Returns:
            str: A string representation of the Rectangle instance.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor method that is called when an instance of
        Rectangle is deleted.
        Decrements the class attribute `number_of_instances`
        by 1 and prints a message.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
