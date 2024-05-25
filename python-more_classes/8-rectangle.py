#!/usr/bin/python3

"""
This module defines the Rectangle class
"""


class Rectangle:
    """
    A class representing a rectangle.

    Class attributes:
        number_of_instances (int): the number of Rectangle instances
        print_symbol (str): symbol used for Rectangle representation

    Instance attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is less than 0.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        # Created a new Rectangle, updating number_of_instances
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Returns a string representation of the Rectangle, using the attribute
        print_symbol
        """
        output = ""

        if self.__height == 0 or self.__width == 0:
            return output

        for line in range(0, self.__height):
            for column in range(0, self.__width):
                output += str(self.print_symbol)
            # Not adding a newline after last line of the rectangle
            if line != (self.__height - 1):
                output += "\n"
        return output

    def __repr__(self):
        """
        Returns a string representation of the Rectangle object.

        Can be used to create a new object with eval():
            >>> my_rectangle = Rectangle(2, 4)
            >>> new_rectangle = eval(repr(my_rectangle))
            >>> print(type(new_rectangle) is type(my_rectangle))
            True
        """
        return (f'Rectangle({self.width}, {self.height})')

    def __del__(self):
        """
        Prints a message when the rectangle object is deleted.

        Also updates the number_of_instances attribute of the
        Rectangle class to count the deletion
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares the area of two Rectangle objects and returns the one with
        the bigger area. If the two rectangles have the same area, returns
        rect_1.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Raises:
            TypeError: If rect_1 or rect_2 are not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the bigger area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @property
    def height(self):
        """
        Gets the height of the rectangle.
        """
        return self.__height

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        """
        return self.__width

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            If height or width are 0, returns 0.
            Otherwise, returns the perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))
