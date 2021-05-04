#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list[:]
    len_list = len(my_list)
    if idx < 0 or idx >= len_list:
        return list_copy
    else:
        list_copy[idx] = element
    return list_copy
