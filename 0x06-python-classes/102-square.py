#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initializes a new Square object.

        Args:
            size (int): The size of the square. Must be a positive integer.
        """
        if not isinstance(size, (float, int)):
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size to set. Must be a positive integer.

        Raises:
            TypeError: If the value is not a number (float or integer).
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
