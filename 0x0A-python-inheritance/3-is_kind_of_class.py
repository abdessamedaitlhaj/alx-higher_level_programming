#!/usr/bin/python3
"""
Module that defines a function that return true
if the object is an instance of, or if the object is an
instance of a class that inherited from, the
specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Check if is instance"""
    return isinstance(obj, a_class)
