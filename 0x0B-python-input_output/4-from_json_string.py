#!/usr/bin/python3
"""
Module that defines a function that returns an object
(Python data structure) represented by a JSON string
"""


def from_json_string(my_str):
    """Descode json string

        Args:
            my_str(str): desired string to be decoded

        Return:
            the decoded string
    """
    return json.loads(my_str)
