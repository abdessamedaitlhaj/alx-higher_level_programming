#!/usr/bin/python3
"""Module that defines a Square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class with size attribute"""
    def __init__(self, size):
        """Constructor for Square class

            Args:
                size (int): square size
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculate the square area

            Return:
                the square area
        """
        return self.__size * self.__size

    def __str__(self):
        """Overide str method

        Return:
            string
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
