#!/usr/bin/python3
"""
Module that defines script that adds all arguments
to a Python list, and then save them to a file
"""
import sys
import json
save_json = __import__("5-save_to_json_file")
load_json = __import__("6-load_from_json_file")


my_list = []

my_list += load_json.load_from_json_file("add_item.json")

for arg in sys.argv[1:]:
    my_list.append(arg)

save_json.save_to_json_file(my_list, "add_item.json")
