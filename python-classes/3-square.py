#!/usr/bin/python3

"""Square Class

This class is used to cast squares.

"""


class Square:
    """
    Defines a square class

    Methods :
        __init__(self, size): Initialize a square of a given size.

        area(self): returns the current square area.

    """
    def __init__(self, size=0):
        """__init__
        Create a new square instance,
        with a private instance attribute : size

        Attributes :
            __size (int): The size of the square

        Raises :
            TypeError : If 'size' type is not 'int'.

            ValueError : If 'size' value is strictly less than 0.

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """area
        Returns the current square area

        """
        return (self.__size ** 2)
