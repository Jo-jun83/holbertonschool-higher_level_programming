#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element in a list with another element.

    Args:
        my_list (list): The list to search and replace elements in.
        search: The element to search for in the list.
        replace: The element to replace the searched element with.

    Returns:
        list: A new list with the searched elements replaced by the new element
    """
    new_list = []
    for i in my_list:
        if i == search:
            search = replace
            new_list.append(replace)
        else:
            new_list.append(i)
    return new_list
