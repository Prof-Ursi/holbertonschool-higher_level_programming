#!/usr/bin/python3

"""
This module contains a function for reading
and printing the contents of a file.
"""


class Student:
    """
    A class representing a student.

    Attributes:
        first_name (str): the first name of the student.
        last_name (str): the last name of the student.
        age (int): the age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student object.

        Args:
            first_name (str): the first name of the student.
            last_name (str): the last name of the student.
            age (int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts a Student object to a dictionary.

        Returns:
            dict: a dictionary representation of the
            Student object for JSON serialization.
        """
        return self.__dict__
