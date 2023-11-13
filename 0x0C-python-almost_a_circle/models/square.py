#!/usr/bin/python3
"""
Updated class Square with the public method update.
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
            self.id, self.size, self.x, self.y = args[:4]

        # Handle keyword arguments
        for key, value in kwargs.items():
            setattr(self, key, value)


if __name__ == "__main__":
    pass
