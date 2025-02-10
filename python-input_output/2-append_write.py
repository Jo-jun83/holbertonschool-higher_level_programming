#!/usr/bin/python3
"""
This module provides a function to append text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns
    the number of characters added.
    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
