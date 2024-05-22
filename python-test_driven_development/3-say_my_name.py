#!/usr/bin/python3
"""
This module defines a function say_my_name(first_name, last_name="")
that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    Args:
        first_name (str): first name to print
        last_name (str)

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
