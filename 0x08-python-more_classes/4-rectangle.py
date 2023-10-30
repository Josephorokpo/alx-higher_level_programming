#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """
    Defines a Rectangle class with width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width of the Rectangle.

        Returns:
            int: The width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the Rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the Rectangle.

        Returns:
            int: The height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the Rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the Rectangle.

        Returns:
            int: The area of the Rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the Rectangle.

        Returns:
            int: The perimeter of the Rectangle (2 * (width + height)).
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the Rectangle using '#' characters.

        Returns:
            str: A string representation of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = ['#' * self.__width for _ in range(self.__height)]
        return '\n'.join(rect)

    def __repr__(self):
        """
        Return a string representation of the Rectangle that \
                can recreate the object.

        Returns:
            str: A string representation of the Rectangle in the format \
                    "Rectangle(width, height)".
        """
        return f"Rectangle({self.__width}, {self.__height})"
