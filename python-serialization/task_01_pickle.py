#!/usr/bin/python3
"""
This module provides functionality for serializing and deserializing
a custom object using the pickle module.
"""


import pickle


class CustomObject:
    """
    A class used to represent a Custom Object.
    """
    def __init__(self, name, age, is_student):
        """
        Initializes a new instance of the class.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serializes the current object to a file using pickle.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            return True
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.
        Returns:
            object: The deserialized object.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
