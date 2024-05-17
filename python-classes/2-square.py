#!/usr/bin/python3

"""Square Class

This class is used to cast squares.

"""


class Square:
    def __init__(self, size=0):
        """
        Create a new square instance,
        with a private instance attribute : size

        Attributes :
            size (int): The size of the square

        Raises :
            TypeError : If 'size' type is not 'int'.

            ValueError : If 'size' value is strictly less than 0.

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
