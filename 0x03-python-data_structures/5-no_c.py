#!/usr/bin/python3
def no_c(my_string):
    """removes all characters c and C from a string"""
    list_string = list(my_string)
    for i in list_string[:]:
        if (i == 'c') or (i == 'C'):
            list_string.remove(i)
    return ("".join(list_string))
