#!/usr/bin/python3

"""
This module divides all elements of a matrix by a given divisor.
and return A new matrix with each element divided by the divisor
"""


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
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
