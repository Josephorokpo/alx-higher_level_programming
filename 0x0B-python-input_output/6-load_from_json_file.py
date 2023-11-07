#!/usr/bin/python3
"""
Function that creates an Object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read and convert
        to a Python object.

    Returns:
        object: The Python object created from the JSON data in the file.

    Note:
        If the JSON data in the file cannot be converted to a Python object,
        no exceptions are managed.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
