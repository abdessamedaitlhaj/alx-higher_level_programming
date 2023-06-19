#!/usr/bin/python3
"""Module that defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class with new attribute size"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the attributes size, x, y and id"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overiding str method

            Returns:
                Costume output for Square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter method to retrieve size

            Returns:
                the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter method to set size

            Args:
                value (int): the Square's size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute

            Args:
                args (str): list of args
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
                self.__height = args[1]
            if len(args) >= 3:
                self.__x = args[3]
            if len(args) >= 4:
                self.__y = args[4]
        if kwargs:
            if "id" in kwargs:
                self.id = kwargs['id']
            if "size" in kwargs:
                self.__width = kwargs['size']
                self.__height = kwargs['size']
            if "x" in kwargs:
                self.__x = kwargs['x']
            if "y" in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """Returns the dictionary representation

            Returns:
                dictionary representation of a square
        """
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }
