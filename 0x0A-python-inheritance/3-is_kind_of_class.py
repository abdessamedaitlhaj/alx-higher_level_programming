#!/usr/bin/python3
"""Module that defines a is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """is obj an instance of a_class?

        Return:
            True or False
    """
    return isinstance(obj, a_class)
