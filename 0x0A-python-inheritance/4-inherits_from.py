#!/usr/bin/python3
"""Returns True or False"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class inherited \
            (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if the object is an instance of a class that inherited \
                from the specified class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
