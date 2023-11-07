#!/usr/bin/python3
"""Reads a text file (UTF8) and prints its content to stdout."""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None

    Note:
        This function does not handle file permission or file
        existence exceptions.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')

    except Exception as e:
        print(f"An error occurred: {str(e)}")
