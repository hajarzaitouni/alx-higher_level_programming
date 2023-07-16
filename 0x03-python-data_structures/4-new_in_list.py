#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ replaces an element in a list at a specific position
    without modifying the original list (like in C)"""
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    cp_list = my_list.copy()
    cp_list[idx] = element
    return (cp_list)
