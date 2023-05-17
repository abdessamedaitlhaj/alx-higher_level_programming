#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    my_list = list(set_1) + list(set_2)
    return list(filter(lambda elem: my_list.count(elem) == 1, my_list))
