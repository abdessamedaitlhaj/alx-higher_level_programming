#!/usr/bin/python3
string = ""
def remove_char_at(str, n):
    if n < 0 or n == 0:
        return str
    else:
        string = str[:n]
        string += str[n + 1:]
    return string
