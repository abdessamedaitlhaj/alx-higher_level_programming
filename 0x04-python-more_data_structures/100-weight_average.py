#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    dominator = 0
    denominator = 0
    for item in my_list:
        dominator += item[0] * item[1]
    for item in my_list:
        denominator += item[1]
    return dominator / denominator
