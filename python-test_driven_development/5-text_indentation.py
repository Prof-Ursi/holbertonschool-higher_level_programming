#!/usr/bin/python3
"""
This module defines a function text_indentation(text)
that prints the input text with two new lines after each '.', '?' and ':'.
"""


def text_indentation(text):

    """
    Prints the input text with two new lines after each '.', '?' and ':'.

    Args:
        text (str): The input text to process.

    Raises:
        TypeError: If the input text is not a string.
    """

    if type(text) is not (str):
        raise TypeError("text must be a string")

    sentence = ""

    for character in text:
        sentence += character

        if character in [".", "?", ":"]:
            print("{}\n".format(sentence.strip()))
            sentence = ""

    if sentence.strip() != "":
        print("{}".format(sentence.strip()), end="")
