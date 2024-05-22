#!/usr/bin/python3
"""
This module defines a function print_square(size)
that prints a square with '#' of a defined size.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): size length of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: if size is < 0

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("")
    else:
        for i in range(size):
            print("#" * size)
