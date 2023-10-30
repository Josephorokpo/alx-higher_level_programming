#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """
    This class defines a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Class Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.

    Methods:
        __init__(self, width=0, height=0): Initializes a Rectangle \
                instance with optional width and height.
        area(self): Calculate and return the area of the rectangle.
        perimeter(self): Calculate and return the perimeter of the rectangle.
        __str__(self): Return a string representation of the \
                rectangle using the print_symbol.
        __repr__(self): Return a string representation for \
                recreating the instance.
        __del__(self): Print a message when an instance of \
                Rectangle is deleted.
        static bigger_or_equal(rect_1, rect_2): Return the rectangle \
                with the bigger or equal area.
        classmethod square(cls, size=0): Create a new Rectangle \
                instance as a square.

    Static Methods:
        bigger_or_equal(rect_1, rect_2): Return the rectangle with \
                the bigger or equal area.

    Class Methods:
        square(cls, size=0): Create a new Rectangle instance as a square.

    """

    number_of_instances = 0  # Initialize the class attribute
    print_symbol = "#"

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
        Return a string representation of the rectangle using print_symbol.

        Returns:
            str: A string representing the rectangle using print_symbol.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the bigger or equal area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the bigger or equal area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a new Rectangle instance as a square.

        Args:
            size (int, optional): The size of the square \
                    (both width and height). Defaults to 0.

        Returns:
            Rectangle: A new Rectangle instance representing a square.
        """
        return cls(size, size)
