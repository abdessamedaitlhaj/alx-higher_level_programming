#!/usr/bin/python3
"""Module that define lookup function"""


def lookup(obj):
    """Return the list of available attributes and
        methods of an object

        Return:
            the list of attributes and methods
    """
    return dir(obj)
