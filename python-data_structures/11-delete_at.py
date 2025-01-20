#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Args:
        my_list (list): The list from which the item will be deleted.
        idx (int): The index of the item to delete. If the index is negative or
                out of range, the list remains unchanged.

    Returns:
        list: The modified list with the item removed if the index is valid,
            otherwise the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del my_list[idx]
        return my_list
