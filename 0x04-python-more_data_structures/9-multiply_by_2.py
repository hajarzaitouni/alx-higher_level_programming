#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """all the dictionary values multiplied by 2"""
    new_dic = a_dictionary.copy()
    for k in new_dic.keys():
        new_dic[k] *= 2
    return (new_dic)
