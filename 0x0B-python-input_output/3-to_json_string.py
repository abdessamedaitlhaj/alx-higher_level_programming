#!/usr/bin/python3
"""Module eturns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """Return JSON representation of an object

        Args:
            my_obj(object): the object to be formatted

        Return:
            the JSON format
    """
    return my_obj.json
