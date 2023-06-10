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

    @property
    def size(self):
        """Getter method to retrieve size

            Return:
                the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set size

            Args:
                value (int): the size of the sqaure

            Raises:
                TypeError size must be an integer
                ValueError size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square

            Return:
                the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """print square as # to stdout"""
        if self.__size == 0:
            print()
        else:
            print(("#" * self.__size + "\n") * self.__size, end="")
