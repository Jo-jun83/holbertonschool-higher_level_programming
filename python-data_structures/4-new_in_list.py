#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific position
    without modifying the original list.

    Args:
        my_list (list): The original list.
        idx (int): The index at which to replace the element.
        element: The new element to be placed at the specified index.

    Returns:
        list: A new list with the element replaced at
        the specified index if the index is valid.
        If the index is out of range, returns a copy of the original list.
    """
    copy = my_list.copy()
    if idx < 0:
        return copy
    elif idx >= len(my_list):
        return copy
    copy[idx] = element
    return copy
