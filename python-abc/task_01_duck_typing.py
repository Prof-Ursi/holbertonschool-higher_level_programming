#!/usr/bin/python3

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to be implemented by subclasses.
        Returns the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to be implemented by subclasses.
        Returns the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Concrete subclass of Shape representing a circle.

    Instance attribute :
        radius: the radius of the circle.
    """

    def __init__(self, radius):
        """
        Initializes a new instance of the Circle class.

        Args :
            radius (float, int): the radius of the circle.

        Raises:
            TypeError: If radius is neither a float nor an integer.
            ValueError: If radius is less than 0.
        """
        if not isinstance(radius, (float, int)):
            raise TypeError("radius must be either an integer or a float")
        if radius < 0:
            raise ValueError("radius must be a positive number.")
        self.radius = radius

    def area(self):
        """
        Implementation of the area method for circles.
        Returns the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Implementation of the perimeter method for circles.
        Returns the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete subclass of Shape representing a rectangle.

    Instance attribute :
        - width (float, int): the width of the rectangle.
        - height (float, int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a new instance of the Rectangle class.

        Args :
            - width (float, int): The width of the rectangle.
            - height (float, int): The height of the rectangle.

        Raises:
            - TypeError: If either height or width is
            neither a float nor an integer.
            - ValueError: If either height or width is less than 0.
        """
        if not isinstance(height, (float, int)):
            raise TypeError("height must be either an integer or a float")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height = height

        if not isinstance(width, (float, int)):
            raise TypeError("width must be either an integer or a float")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = width

    def area(self):
        """
        Implementation of the area method for rectangles.
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Implementation of the perimeter method for rectangles.
        Returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Concrete class method that takes shape into argument and calls
    the shape area and perimeter methods to print them.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
