#!/usr/bin/python3
"""
Updated class Base with added static method to_json_string
"""


import json


class Base:
    """
    Base class for other classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation.

        :param list_dictionaries: List of dictionaries to convert.
        :return: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        :param json_string: JSON string to convert.
        :return: List of dictionaries represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set using a dictionary.

        :param dictionary: Dictionary containing attribute values.
        :return: Instance with attributes set.
        """
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a file.

        :return: List of instances.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save instances to a file.

        :param list_objs: List of instances.
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding='utf-8') as file:
            list_dicts = [obj.to_dictionary() for obj in list_objs] if list_objs is not None else []
            file.write(cls.to_json_string(list_dicts))
