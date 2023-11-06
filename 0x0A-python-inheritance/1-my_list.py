#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """
    MyList is a custom list class that inherits from the built-in list class.
    It includes additional methods for custom operations.

    Attributes:
        None

    Methods:
        print_sorted(self): Print the elements of the list in ascending \
                sorted order.
    """

    def print_sorted(self):
        """
        Print the elements of the list in ascending sorted order.

        Args:
            None

        Returns:
            None

        Example:
        >>> my_list = MyList([3, 1, 2, 4])
        >>> my_list.print_sorted()
        [1, 2, 3, 4]
        """
        sorted_list = sorted(self)
        print(sorted_list)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
