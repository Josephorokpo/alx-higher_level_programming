#!/usr/bin/python3
"""
A function that returns the JSON representation \
        of an object (string)
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of the given object as a string.

    Args:
        my_obj: The object to be converted to a JSON string.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
