#!/usr/bin/python3
"""
Module that defines script that adds all arguments
to a Python list, and then save them to a file
"""
import sys
import json
save_json = __import__("5-save_to_json_file")


my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

with open("add_item.json", "a", encoding="utf-8") as file:
    save_json.save_to_json_file(my_list, "add_item.json")
