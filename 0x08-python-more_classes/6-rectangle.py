#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """
    This class defines a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Class Attribute:
        number_of_instances (int): The number of Rectangle instances.

    Methods:
        __init__(self, width=0, height=0): Initializes a Rectangle \
                instance with optional width and height.
        area(self): Calculate and return the area of the rectangle.
        perimeter(self): Calculate and return the perimeter of the rectangle.
        __str__(self): Return a string representation of the rectangle.
        __repr__(self): Return a string representation for \
                recreating the instance.
        __del__(self): Print a message when an instance of \
                Rectangle is deleted.
    """

    number_of_instances = 0  # Initialize the class attribute

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with optional width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.

        Raises:
            ValueError: If width or height is less than 0.
            TypeError: If width or height is not an integer.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment the number of instances

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            ValueError: If width is less than 0.
            TypeError: If width is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            ValueError: If height is less than 0.
            TypeError: If height is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height)).
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' character.

        Returns:
            str: A string representing the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(['#' * self.width] * self.height)

    def __repr__(self):
        """
        Return a string representation for recreating the instance.

        Returns:
            str: A string representation for recreating the Rectangle instance.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Print a message when an instance of Rectangle is deleted.
        Decrement the number of instances.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
