#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """deletes keys with a specific value in a dictionary"""
    new_dic = a_dictionary.copy()
    for key in new_dic.keys():
        if new_dic[key] == value:
            del a_dictionary[key]
    return a_dictionary
