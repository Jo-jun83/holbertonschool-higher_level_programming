#!/usr/bin/python3
"""
This module provides a function to convert a CSV file to a JSON file.
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Converts a CSV file to a JSON file.
    Returns:
        bool: True if the conversion was successful,
        False if the file was not found.
    """
    try:
        with open(filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)
        return True

    except FileNotFoundError:
        print("file not found")
        return False
