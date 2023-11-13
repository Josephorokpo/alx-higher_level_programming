#!/usr/bin/python3
"""
Updated class Square with the public getter and setter size.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class.

        :param size: Size of the square.
        :param x: X-coordinate of the square (default is 0).
        :param y: Y-coordinate of the square (default is 0).
        :param id: ID of the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute."""
        self.width = value
        self.height = value


if __name__ == "__main__":
    pass
