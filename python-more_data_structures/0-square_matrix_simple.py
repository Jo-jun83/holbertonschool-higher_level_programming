#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Args:
        matrix (list of list of int): A 2-dimensional list of integers.

    Returns:
        list of list of int: A new matrix with the square of each integer
        from the input matrix.
    """
    new_matrix = []
    for row in matrix:
        new_row = [x ** 2 for x in row]
        new_matrix.append(new_row)
    return new_matrix
