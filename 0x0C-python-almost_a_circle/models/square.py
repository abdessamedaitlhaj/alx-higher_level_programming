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
        if len(args) >= 1:
            if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[3]
            if len(args) >= 4:
                self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs['id']
            if "size" in kwargs:
                self.width = kwargs['size']
                self.height = kwargs['size']
            if "x" in kwargs:
                self.x = kwargs['x']
            if "y" in kwargs:
                self.y = kwargs['y']

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
