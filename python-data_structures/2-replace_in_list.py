#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific position.

    Args:
        my_list (list): The list in which the element will be replaced.
        idx (int): The index at which the element will be replaced.
        element: The new element to be placed at the specified index.

    Returns:
        list: The modified list with the new element at the specified index.
            If idx is out of range, the original list is returned unchanged.
    """
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
