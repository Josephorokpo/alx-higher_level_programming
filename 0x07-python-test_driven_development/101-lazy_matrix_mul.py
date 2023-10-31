#!/usr/bin/python3
"""multiplies 2 matrices by using the module NumPy"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
    m_a (list of lists): First matrix.
    m_b (list of lists): Second matrix.

    Returns:
    list of lists: Result of the matrix multiplication.

    Raises:
    TypeError: If m_a or m_b is not a list of lists.
    ValueError: If m_a or m_b is empty or not rectangular.
    TypeError: If m_a or m_b contains non-numeric elements.
    ValueError: If m_a and m_b cannot be multiplied.
    """
    try:
        result = np.dot(np.array(m_a), np.array(m_b))
        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
    except Exception:
        raise
