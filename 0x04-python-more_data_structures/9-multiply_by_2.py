#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    values = list(map(lambda value: value * 2, a_dictionary.values()))
    keys = list(a_dictionary.keys())
    new_dict = dict(zip(keys, values))
    return new_dict
