#!/usr/bin/python3
"""
A class Student that defines a student by: (based on 9-student.py.
"""


class Student:
    """
    Defines a student by first name, last name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        to_json(self, attrs=None): Retrieves a dictionary representation of
        a Student instance.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the given attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to
            include in the dictionary.
                If None, all attributes are retrieved.

        Returns:
            dict: A dictionary with the student's attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
