#!/usr/bin/python3
"""
A function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj (object): The object to which the attribute will be added.
        attribute (str): The name of the new attribute.
        value: The value of the new attribute.

    Raises:
        TypeError: If the object can't have a new attribute.

    Note:
        This function raises a TypeError exception with the message
        "can't add new attribute" if the object can't have a new attribute.

    Example:
        >>> obj = object()
        >>> add_attribute(obj, "new_attr", 42)
        >>> print(obj.new_attr)
        42
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[attribute] = value
    else:
        raise TypeError("can't add new attribute")
