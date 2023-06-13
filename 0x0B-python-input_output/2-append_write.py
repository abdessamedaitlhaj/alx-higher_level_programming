#!/usr/bin/python3
"""Module that defines a append_write function"""


def append_write(filename="", text=""):
    """Append the given content to a given file

        Args:
            filename (file): the file name
            text (str): string to be appended

        Return:
            number of character appended
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
