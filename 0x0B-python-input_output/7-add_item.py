#!/usr/bin/python3
"""
Script to add items to a Python list and save it to a JSON file.
"""


import sys
import json
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_items_to_list_and_save(filename, *items):
    """
    Add items to a Python list and save it to a JSON file.

    Args:
        filename (str): The name of the JSON file to save the list to.
        *items: Any number of items to add to the list.

    Returns:
        None
    """
    if path.exists(filename):
        # Load existing list from the file
        my_list = load_from_json_file(filename)
    else:
        # Create a new list if the file doesn't exist
        my_list = []

    # Add the new items to the list
    my_list.extend(items)

    # Save the updated list to the JSON file
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./7-add_item.py <item1> <item2> <item3> ...")
    else:
        filename = "add_item.json"
        items = sys.argv[1:]
        add_items_to_list_and_save(filename, *items)
