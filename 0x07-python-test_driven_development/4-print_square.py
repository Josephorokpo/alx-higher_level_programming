#!/usr/bin/python3
"""prints a square with the character #."""


def print_square(size):
    """
    Prints a square of a given size using the character '#'.

    Args:
    size (int): The size of the square.

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0 or a float.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
