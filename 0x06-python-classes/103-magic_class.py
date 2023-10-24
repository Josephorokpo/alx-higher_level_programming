#!/usr/bin/python3
"""MagicClass that does exactly"""
import math


class MagicClass:
    """A class that represents a magical circle with radius."""

    def __init__(self, radius=0):
        """
        Initializes a new Magical Circle object.

        Args:
            radius (int or float): The radius of the magical circle.
            Default is 0.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Returns the area of the magical circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference of the magical circle."""
        return 2 * math.pi * self.__radius
