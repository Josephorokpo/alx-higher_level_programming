#!/usr/bin/python3
"""A function that writes a string to a text file (UTF8) and returns \
        the number of characters written."""


def write_file(filename="", text=""):
    """
    Writes the given text to a file in UTF-8 encoding and returns \
            the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            # Write the text to the file
            num_characters_written = file.write(text)
            return num_characters_written

    except Exception as e:
        # Handle exceptions if any (e.g., file not found)
        return 0


if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
