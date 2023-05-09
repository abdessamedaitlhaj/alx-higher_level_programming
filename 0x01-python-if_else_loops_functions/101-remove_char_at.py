#!/usr/bin/python3
string = ""
def remove_char_at(str, n):
    if n < 0 or n == 0:
        return str
    else:
        string = str[:n]
        string += str[n + 1:]
    return string
print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
