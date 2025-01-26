#!/usr/bin/python3

"""
This module Adds two new lines after each occurrence
of '.', '?' or ':' in the given text.
"""


def text_indentation(text):
    """
    Adds two new lines after each occurrence
    of '.', '?' or ':' in the given text.

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If the input text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".:?":
            print("\n")
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
