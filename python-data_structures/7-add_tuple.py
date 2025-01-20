#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples element-wise.

    Parameters:
        tuple_a (tuple): The first tuple. Defaults to an empty tuple.
        tuple_b (tuple): The second tuple. Defaults to an empty tuple.

    Returns:
        tuple: A tuple containing the sum of the first two elements
        of each input tuple.
               If a tuple has less than 2 elements, 0 is used as
               the missing element.
               If a tuple has more than 2 elements, only the first
               two are considered.
    """
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
