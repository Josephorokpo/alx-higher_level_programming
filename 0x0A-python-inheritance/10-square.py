#!/usr/bin/python3
"""
A class Square that inherits from Rectangle.
"""


class BaseGeometry:
    """
    This is the BaseGeometry class.

    Methods:
        area(): Placeholder for area calculation.
        integer_validator(name, value): Validates if value is an integer \
                and greater than 0.
    """
    def area(self):
        """
        Placeholder for area calculation.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if value is an integer and greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to validate.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle and inherits from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string in the format "[Rectangle] <width>/<height>"
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    This class represents a square and inherits from Rectangle.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string in the format "[Square] <size>/<size>"
        """
        return f"[Square] {self.__size}/{self.__size}"
