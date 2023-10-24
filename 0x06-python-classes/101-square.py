#!/usr/bin/python3
"""Define a class Square that represents a square."""


class Square:
    """
    Represent a square.

    This class represents a square object. It includes methods to set and
    retrieve the size and position of the square, calculate its area, and
    display it with the '#' character.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get or set the current size of the square.

        The size of the square must be a positive integer.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size to set. Must be a positive integer.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get or set the current position of the square.

        The position must be a tuple of two positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The position to set. Must be a tuple of two
                positive integers.

        Raises:
            TypeError: If the value is not a valid tuple.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculate and return the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square with the '#' character.

        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """
        Define the print() representation of a Square.

        Returns:
            str: A string representation of the square.
        """
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for x in range(0, self.__position[0]]
                [print("#", end="") for y in range(0, self.__size)]
                if i != self.__size - 1:
                    print("")
        return ("")
