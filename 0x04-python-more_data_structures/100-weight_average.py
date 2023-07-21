#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple"""
    if not my_list:
        return 0
    sum_sc_wgt = sum([x * y for x, y in my_list])
    total_wgt = sum([y for x, y in my_list])
    if total_wgt == 0:
        return 0
    return (sum_sc_wgt / total_wgt)
