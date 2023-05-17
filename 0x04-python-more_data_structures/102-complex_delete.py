#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a = a_dictionary.copy()
    for key in a.keys():
        if a[key] == value:
            del a_dictionary[key]
    return a_dictionary
