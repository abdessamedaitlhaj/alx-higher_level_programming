#!/usr/bin/python3
"""Module that defines a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with area() and """
    def area(self):
        """Not defined yet!

            Raises:
                Exception area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a given value

            Args:
                name (str): the name
                value (int): value for the name

            Raises:
                TypeError value must be an integer
                ValueError value must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value <= 0:
            raise ValueError("value must be greater than 0")
