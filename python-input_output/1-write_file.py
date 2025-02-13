#!/usr/bin/python3
"""
This module provides a function to write a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number
    of characters written.
    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        write = f.write(text)
    return len(text)
