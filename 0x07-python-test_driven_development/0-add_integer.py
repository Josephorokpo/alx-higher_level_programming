#!/usr/bin/python3
"""Adds two integers."""


def add_integer(a, b=98):
    """
    Adds two integers.
    
    Args:
    a (int or float): The first number.
    b (int or float, optional): The second number (default is 98).

    Returns:
    int: The sum of a and b, cast to an integer.

    Raises:
    TypeError: If a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)

    # Return the sum of a and b
    return a + b
