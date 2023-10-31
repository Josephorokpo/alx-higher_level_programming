#!/usr/bin/python3
"""multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
    m_a (list of lists): The first matrix.
    m_b (list of lists): The second matrix.

    Returns:
    list of lists: The result of matrix multiplication.

    Raises:
    TypeError: If m_a or m_b is not a list or not a list of lists, or if they contain non-integer and non-float elements.
    ValueError: If m_a or m_b is empty, if m_a and m_b can't be multiplied, or if each row of m_a or m_b is not of the same size.
    """

    # Check if m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    # Check if m_a or m_b is empty
    if len(m_a) == 0 or len(m_b) == 0 or any(len(row) == 0 for row in m_a) or any(len(row) == 0 for row in m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Check if m_a and m_b contain only integers or floats
    if not all(isinstance(x, (int, float)) for row in m_a for x in row) or not all(isinstance(x, (int, float)) for row in m_b for x in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    # Check if each row of m_a and m_b has the same size
    if len(set(len(row) for row in m_a)) != 1 or len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Perform matrix multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

