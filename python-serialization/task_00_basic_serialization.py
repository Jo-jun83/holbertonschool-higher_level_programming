#!/usr/bin/python3
"""
This module provides functions for serializing data to JSON
format and saving it to a file,
as well as loading and deserializing JSON data from a file.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes the given data to JSON format and saves it to a file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file.
    Returns:
        dict: The deserialized JSON data as a Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
