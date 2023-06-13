#!/usr/bin/python3
"""Module that defines a load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Creates an Object from a 'JSON file'

        Args:
            filename (file): name of the file

        Return:
            the decoded object from a file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
