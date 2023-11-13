#!/usr/bin/python3
"""
Square class that inherits from Rectangle.
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

    def update(self, *args, **kwargs):
        """
        Update attributes with the provided arguments.

        :param args: Positional arguments in the order (id, size, x, y).
        :param kwargs: Keyword arguments for attributes (id, size, x, y).
        """
        if args:
            args_count = len(args)
            if args_count >= 1:
                self.id = args[0]
            if args_count >= 2:
                self.size = args[1]
            if args_count >= 3:
                self.x = args[2]
            if args_count >= 4:
                self.y = args[3]

        # Handle keyword arguments
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)


if __name__ == "__main__":
    square = Square(5, 10, 15, 1)
    print(square)
