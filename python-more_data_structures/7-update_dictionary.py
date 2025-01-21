#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Update or add a key-value pair in a dictionary.

    If the key already exists in the dictionary, update its value.
    If the key does not exist, add the key-value pair to the dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key: The key to update or add.
        value: The value associated with the key.

    Returns:
        dict: The updated dictionary.
    """
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary.update({key: value})
    return a_dictionary
