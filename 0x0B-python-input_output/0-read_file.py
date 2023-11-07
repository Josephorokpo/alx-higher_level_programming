#!/usr/bin/python3
"""Reads a text file (UTF8) and prints it to stdout."""


def write_file(filename="", text=""):
    """
    Writes the given text to a file in UTF-8 encoding.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            # Write the text to the file
            file.write(text)

            # Calculate and return the number of characters written
            num_characters_written = len(text)
            return num_characters_written

    except Exception as e:
        # Handle exceptions if any (e.g., file not found)
        print(f"An error occurred: {str(e)}")
        return (0)
