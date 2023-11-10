#!/usr/bin/python3
"""Class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        :param width: Width of the rectangle.
        :param height: Height of the rectangle.
        :param x: X-coordinate of the rectangle (default is 0).
        :param y: Y-coordinate of the rectangle (default is 0).
        :param id: ID of the rectangle (default is None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute."""
        if not isinstance(value, int):
            raise ValueError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute."""
        if not isinstance(value, int):
            raise ValueError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute."""
        if not isinstance(value, int):
            raise ValueError("X must be an integer")
        if value < 0:
            raise ValueError("X must be greater than or equal to 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute."""
        if not isinstance(value, int):
            raise ValueError("Y must be an integer")
        if value < 0:
            raise ValueError("Y must be greater than or equal to 0")
        self.__y = value
