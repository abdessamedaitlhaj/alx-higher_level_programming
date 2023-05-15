#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lenght = len(my_list)
    for i in range(lenght):
        print("{:d}".format(my_list[lenght - i - 1]))
