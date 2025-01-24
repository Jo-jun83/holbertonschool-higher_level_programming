#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of list of int/float): A list of lists where each inner list represents a row of the matrix.
        div (int/float): The divisor by which each element of the matrix will be divided.

    Returns:
        list of list of float: A new matrix with each element divided by the divisor, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats, or if the rows of the matrix are not of the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is zero.
    """
    new_matrix = []
    if type(matrix) not in [int, float]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) != matrix[1]:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0
        raise ZeroDivisionError("division by zero")
    return new_matrix
