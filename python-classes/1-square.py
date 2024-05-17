#!/usr/bin/python3

"""Square Class

This class is used to cast squares.

"""


class Square:
    def __init__(self, size):
        """
        Create a new square instance,
        with a private instance attribute : size

        Arguments :
            size (int): The size of the square
        """
        self.__size = size
