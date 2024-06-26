#!/usr/bin/python3
"""
This module defines a function that reads a text file and prints it.
"""


def read_file(filename=""):
    """
    Reads a text file in UTF8 and prints it to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
