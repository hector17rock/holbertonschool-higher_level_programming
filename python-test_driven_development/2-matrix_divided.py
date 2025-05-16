#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
Each element is divided by a divisor and rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and returns a new matrix.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (int or float) to divide by.

    Returns:
        A new matrix with the result of the division.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
