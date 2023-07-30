#!/usr/bin/python3
"""
Module that check if an object is an instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    Function eturns True if the object is exactly an instance
    of the specified class ; otherwise False
    """
    return type(obj) == a_class
