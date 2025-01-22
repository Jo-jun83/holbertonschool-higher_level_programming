#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value from a dictionary.

    Args:
        a_dictionary (dict): A dictionary where keys are strings
        and values are integers.

    Returns:
        str: The key with the highest integer value. If the dictionary
        is empty or None, returns None.
    """
    if not a_dictionary:
        return None
    max_value = 0
    max_key = None
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
