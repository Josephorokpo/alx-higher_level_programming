#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry:
    """
    This is the BaseGeometry class.

    It serves as a base class for geometric operations and shapes.

    Public Methods:
    - area(self): Raises an Exception with the message "area() \
            is not implemented."
    - integer_validator(self, name, value): Validates an integer \
            value with specific criteria.

    Attributes:
    - name: A string representing the name of the value.
    - value: An integer value to be validated.
    """

    def area(self):
        """
        Raise an Exception with the message "area() is not implemented."

        This method is designed to be overridden by subclasses to \
                calculate the area of specific geometric shapes.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value with specific criteria.

        Args:
        - name (str): The name of the value being validated.
        - value (int): The integer value to be validated.

        Raises:
        - TypeError: If the value is not an integer, with the message \
                "<name> must be an integer."
        - ValueError: If the value is less than or equal to 0, with the \
                message "<name> must be greater than 0."
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
