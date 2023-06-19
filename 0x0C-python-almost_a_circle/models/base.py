#!/usr/bin/python3
"""Module that contains Base class"""
import os
import json


class Base:
    """Base class with id attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method to set id attribute

            Args:
                id (int): the id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert list of dictionaries into JSON

            Args:
                 list_dictionaries (dic): list of dictionaries

            Returns:
                JSON string representation of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Convert list of boject to JSON and save it to a file

            Args:
                list_objs (object): list of objects
        """
        if list_objs is None or list_objs == []:
            content = "[]"
        else:
            content = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]
                    )
            with open(cls.__name__ + ".json", "w") as f:
                f.write(content)

    @staticmethod
    def from_json_string(json_string):
        """Return a list of JSON string

            Args:
                json_string (JSON): JSON string

            Returns:
                list of JSON string
        """
        if json_string is None or json_string == '':
            return "[]"
        from_json = json.loads(json_string)
        return from_json

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set

                Args:
                    **dictionary (list): keyworded argument

                Returns:
                    the new instance
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances

            Returns:
                list of instances
        """
        my_list = []
        if not os.path.exists(cls.__name__ + ".json"):
            return my_list
        else:
            with open(cls.__name__ + ".json", "r", encoding='utf-8') as f:
                decoded_json_string = cls.from_json_string(f.read())
            for dic in decoded_json_string:
                my_list.append(cls.create(dic))
            return my_list
