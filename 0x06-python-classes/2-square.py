#!/usr/bin/python3
"""Module that defines a square"""


class Square:
    """Square class that defines a square"""

    def __init__(self, size=0):
        """Initialization of the attribute size

            Args:
                size (int): the size of the square

            Raises:
                TypeError size must be an integer
                ValueError size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
