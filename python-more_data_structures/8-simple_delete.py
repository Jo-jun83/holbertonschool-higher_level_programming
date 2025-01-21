#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Args:
        a_dictionary (dict): The dictionary from which to delete the key.
        key (str): The key to delete from the dictionary. Defaults to an
        empty string.

    Returns:
        dict: The dictionary with the specified key removed, if it exists.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    else:
        return a_dictionary
    return a_dictionary
