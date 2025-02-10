#!/usr/bin/python3
"""
This module defines a function `class_to_json` that returns the dictionary
description with simple data structure (list, dictionary, string, integer,
and boolean) for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Converts an object's attributes to a dictionary representation.

    Returns:
        A dictionary containing all the attributes of the object.
    """
    return obj.__dict__
