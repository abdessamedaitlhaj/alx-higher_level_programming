#!/usr/bin/python3
"""module defines a Rectangle class"""


class Rectangle:
    """class that represents a rectangle with attributes width and height"""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with the specified width and height

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method to retrieve the width of the rectangle

            Return:
                the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the width of the rectangle

            Args:
                value (int): the value of the width

            Raises:
                TypeError width must be an integer
                ValueError width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve the height of the rectangle

            Return:
                the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the height of the rectangle

            Args:
                value (int): the value of the height

            Raises:
                TypeError height must be an integer
                ValueError height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method for area calculation

            Return:
                the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Method for perimeter calculation

            Return:
                the perimiter of the rectangle
        """
        if not self.__width or not self.__height:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(slef):
        """Overwrite str to print rectangle as #

            Return:
                string of #
        """
        if not self.__width and not self.__height:
            return ("#" * self.__width + "\n") * (self.__height - 1) + \
                "#" * self.__width
        else:
            return ""
