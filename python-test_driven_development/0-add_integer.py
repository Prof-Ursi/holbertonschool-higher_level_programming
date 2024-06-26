#!/usr/bin/python3

"""
Function that adds two integers

"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first integer or float to be added.
        b (int or float): The second integer or float to be added.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is neither an integer nor float.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
