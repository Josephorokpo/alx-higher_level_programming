#!/usr/bin/python3
"""Reads a text file (UTF8) and prints its content to stdout."""


def read_file(filename=""):
    """
    Reads the content of the given file and prints it to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Read the content of the file and print it to stdout
            print(file.read())

    except Exception as e:
        # Handle exceptions if any (e.g., file not found)
        pass


if __name__ == "__main__":
    read_file("my_file_0.txt")
