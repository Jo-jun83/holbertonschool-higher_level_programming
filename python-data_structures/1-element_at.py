#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Retrieve an element from a list at a specific index.

    Args:
        my_list (list): The list from which to retrieve the element.
        idx (int): The index of the element to retrieve.

    Returns:
        The element at the specified index in the list if the index is valid.
        If the index is negative or out of range, returns None.
    """
    for i in my_list:
        if idx < 0:
            return None
        elif idx > len(my_list):
            return None
        else:
            return my_list[idx]
