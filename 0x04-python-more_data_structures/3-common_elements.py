#!/usr/bin/python3
def common_elements(set_1, set_2):
    my_list = list(set_1) + list(set_2)
    return list(set((filter(lambda item: my_list.count(item) == 2, my_list))))
