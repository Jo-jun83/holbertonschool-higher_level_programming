#!/usr/bin/python3
"""
This module defines a `Student` class.
"""


class Student:
    """
    A class used to represent a Student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts the instance attributes to a dictionary representation.
        """
        return self.__dict__
