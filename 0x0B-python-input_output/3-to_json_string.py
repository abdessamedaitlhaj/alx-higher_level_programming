#!/usr/bin/python3
import json
"""Module that defines to_json_string function"""


def to_json_string(my_obj):
    """Convert an obj to a json format

        Args:
            my_obj (object): the object to be coverted

        Return:
            the json formt of the given object
    """
    return json.dumps(my_obj)
