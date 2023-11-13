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
            # Update id, size, x, y if provided
            self.id = args[0] if len(args) > 0 else self.id
            self.size = args[1] if len(args) > 1 else self.size
            self.x = args[2] if len(args) > 2 else self.x
            self.y = args[3] if len(args) > 3 else self.y

        # Handle keyword arguments
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square.
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
