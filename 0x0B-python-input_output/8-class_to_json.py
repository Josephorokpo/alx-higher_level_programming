#!/usr/bin/python3
"""
A function that returns the dictionary description with simple data
structure (list, dictionary, string, integer and boolean) for JSON
serialization of an objectScript to add items to a Python list and
save it to a JSON file.
"""


def class_to_json(obj):
    """
    Convert an object to a dictionary for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object's attributes.

    Note:
        The function works for objects with attributes that are
        lists, dictionaries,
        strings, integers, and booleans. Other types may not be supported.
    """
    # Create an empty dictionary to store attribute-value pairs
    json_dict = {}

    # Iterate through the object's attributes
    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            # Check if the attribute value is of a serializable type
            json_dict[attr_name] = attr_value

    return (json_dict)
