#!/usr/bin/python3
"""
A function that inserts a line of text to a file, after each line
containing a specific string .
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text into a file after each line containing a specific
    search string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after each matching line.

    Returns:
        None
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        with open(filename, 'w') as file:
            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string + '\n')

    except Exception as e:
        # Handle exceptions if any (e.g., file not found)
        print(f"An error occurred: {str(e)}")
