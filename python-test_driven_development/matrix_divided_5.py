#!/usr/bin/python3
"""
Module for matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number and returns a new matrix.

    Args:
        matrix (list): a list of lists of integers or floats
        div (int/float): number to divide by

    Returns:
        list: A new matrix with elements divided by div and rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows of matrix have different sizes
        TypeError: If div is not a number
        ZeroDivisionError: If div is 0
    """
    # Check if matrix is a list
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size and contain only integers/floats
    row_size = None
    for row in matrix:
        # Check if row is a list
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        # Set row_size if not set yet
        if row_size is None:
            row_size = len(row)
        # Check if current row has the same size as the first row
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        # Check if all elements in the row are integers or floats
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix with elements divided by div and rounded to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix

