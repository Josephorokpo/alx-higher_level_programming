#!/usr/bin/python3
"""Class Base"""


class Base:
    """
    Base class for managing id attribute in all future classes.
    """

    # private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        If id is provided, assign it to the public instance attribute id.
        Otherwise, increment __nb_objects and assign the new value to id.

        :param id: An integer representing the id (optional).
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
