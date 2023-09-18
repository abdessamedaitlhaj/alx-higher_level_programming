#!/usr/bin/python3
"""
Module that defines a function that returns an object
(Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """ Function returns an object as JSON

    Args:
        my_str: JSON representation

    Raises:
        Exception: string can't be decoded

    """
    return json.loads(my_str)
