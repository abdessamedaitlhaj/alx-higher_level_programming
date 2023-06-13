#!/usr/bin/python3
import json
"""Module that defines from_json_string function"""


def from_json_string(my_str):
    """Decode the object

        Args:
            my_str (JSON): represent JSON string format

        Return:
            returns an object
    """
    return json.load(my_str)
