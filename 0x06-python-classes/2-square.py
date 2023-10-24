#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class that defines a square."""

    def __init__(self, size):
        """Initializes a new Square object.

        Args:
            size (int): The size of the square. Must be a positive integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            rise ValueError("size must be >= 0")
        self.__size = size
