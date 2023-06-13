#!/usr/bin/python3
"""Module that defines Student class"""


class Student:
    """Student class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Constructor for the class Student

            Args:
                first_name (str): student's first name
                last_name (str): student's last name
                age (int): student's age

            Raises:
                TypeError age must be an integer
        """
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a dictionary
            representation of a student

            Args:
                attrs (list): list of attributes to retrieve

            Return:
                the dictionary description of the student
        """
        if attrs == None:
            return self.__dict__
        my_dict = {}
        for a in attrs:
            if a in self.__dict__:
                my_dict[a] = self.__dict__[a]
        return my_dict
