#!/usr/bin/python3
"""
A function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate in the Pascal's triangle.

    Returns:
        list of lists: A list of lists representing Pascal's triangle.

    Note:
        Returns an empty list if n is less than or equal to 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        # Generate the next row based on the previous row
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return (triangle)
