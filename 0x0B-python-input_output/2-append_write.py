#!/usr/bin/python3
"""
Module that appends a string at the end of a text
file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """Append text to a file

        Args:
            filename(file): the file to write in
            text(str): the content to be added

        Return:
            the number of char added
    """
    with open(filename, "a+", encoding='utf-8') as f:
        f.write(text)
    return len(text)
