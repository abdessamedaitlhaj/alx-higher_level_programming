#!/usr/bin/python3
"""Module that defines a class_to_json function"""


def class_to_json(obj):
    """Returns the dictionary description

        Args:
            obj (object): object name

        Return:
            the dictionary discription of the obj
    """
    return obj.__dict__
