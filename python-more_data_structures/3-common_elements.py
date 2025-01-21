#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Finds the common elements in two sets.

    Args:
        set_1 (set): The first set of elements.
        set_2 (set): The second set of elements.

    Returns:
        set: A set containing the common elements of set_1 and set_2.
    """
    common = [x for x in set_1 if x in set_2]
    return common
