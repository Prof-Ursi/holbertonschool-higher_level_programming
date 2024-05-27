#!/usr/bin/python3
"""
This module define a function that writes a string to a text files and
returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 text file and returns
    the number of characters written.

    Args :
        filename (str): The name of the file to write into
        text (str): The text to write

    Returns :
        number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
    return len(text)
