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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only the attributes with names
        in this list
        will be retrieved. Otherwise, all attributes will be retrieved.
        Returns:
            dict: Dictionary representation of the instance with the
            specified attributes.
        """
        if attrs is None:
            return self.__dict__

        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result
