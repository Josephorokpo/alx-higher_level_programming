#!/usr/bin/python3
"""Divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
    matrix (list of lists): The matrix to be divided.
    div (int or float): The number to divide by.

    Returns:
    list of lists: A new matrix with elements divided by 'div', \
            rounded to 2 decimal places.

    Raises:
    TypeError: If 'matrix' is not a list of lists of integers or floats.
    TypeError: If each row of 'matrix' does not have the same size.
    TypeError: If 'div' is not a number (integer or float).
    ZeroDivisionError: If 'div' is equal to 0.
    """

    if not isinstance(matrix, list) or not \
            all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")

    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element by 'div' and round to 2 decimal places
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
