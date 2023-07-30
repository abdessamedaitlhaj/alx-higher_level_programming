#!/usr/bin/python3
"""
Module that defines a function that return true if
if the object is an instance of a class that inherited
(directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Check if is an instance
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
