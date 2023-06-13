#!/usr/bin/python3
"""Module that defines a save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using JSON

        Args:
            my_obj (object): the object name
            filename (file): the file name
    """
    width open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
