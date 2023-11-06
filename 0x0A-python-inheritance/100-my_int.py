#!/usr/bin/python3
"""
This module defines a MyInt class that inherits from int and has \
        inverted == and != operators.
"""


class MyInt(int):
    """
    This class represents a MyInt, inheriting from int, with \
            inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Checks if this MyInt is not equal to the other integer.

        Args:
            other (int): The integer to compare.

        Returns:
            bool: True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Checks if this MyInt is equal to the other integer.

        Args:
            other (int): The integer to compare.

        Returns:
            bool: True if equal, False if not equal.
        """
        return super().__eq__(other)
