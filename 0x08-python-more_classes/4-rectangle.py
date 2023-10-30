#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance with optional width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle using '#'.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(['#' * self.width] * self.height)

    def __repr__(self):
        """
        Return a string representation of the rectangle that can recreate a new instance using eval().

        Returns:
            str: A string representation of the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"
