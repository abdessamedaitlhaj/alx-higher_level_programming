#!/usr/bin/python3
"""Module that defines inherits_from function"""


def inherits_from(obj, a_class):
    """check if obj class is a subclass of a_class

        Return:
            True or False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
