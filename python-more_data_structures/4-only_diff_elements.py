#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Return a set of all elements present in only one of the given sets.

    Args:
        set_1 (set): The first set of elements.
        set_2 (set): The second set of elements.

    Returns:
        set: A set containing elements that are unique to each set.
    """
    common = [x for x in set_1 if x not in set_2]
    common_2 = [y for y in set_2 if y not in set_1]
    return common + common_2
