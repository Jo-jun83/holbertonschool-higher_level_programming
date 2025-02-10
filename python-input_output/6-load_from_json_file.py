#!/usr/bin/python3
"""
This module provides a function to load and return the content of a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Load and return the content of a JSON file.
    Returns:
        object: The Python object representation of the JSON file content.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
