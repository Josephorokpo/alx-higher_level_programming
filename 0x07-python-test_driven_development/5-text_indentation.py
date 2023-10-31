#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each '.', '?', and ':'.

    Args:
    text (str): The input text.

    Raises:
    TypeError: If 'text' is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = [".", "?", ":"]
    lines = []

    current_line = ""
    for char in text:
        current_line += char
        if char in punctuations:
            lines.append(current_line.strip())
            current_line = ""

    lines.append(current_line.strip())

    for line in lines:
        print(line)
        print()
