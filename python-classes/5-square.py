#!/usr/bin/python3

"""Square Class

This class is used to cast squares.

"""


class Square:
    """
    Defines a square class

    Methods :
        __init__(self, size): Initialize a square of a given size.

        size(self): getter method to get the size of the square.

        size(self,value): setter method to change the size of the square.

        area(self): returns the current square area.

        my_print(self): prints in stdout the square with the character '#'.

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

    @property
    def size(self):
        """
        Getter method to return the size of the square.

        Returns :
            (int): the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (int): The size of the square. Must be a positive integer.

        Raises:
            TypeError: If the value is not an integer.

            ValueError: If the value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area
        Returns the current square area

        """
        return (self.__size ** 2)

    def my_print(self):
        """my_print
        Prints in stdout the square with the character '#'.

        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
