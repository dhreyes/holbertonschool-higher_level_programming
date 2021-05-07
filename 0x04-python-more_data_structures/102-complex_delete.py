#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = a_dictionary.copy()
    for key, values in new_dic.items():
        if values == value:
            new_dic.pop(key)
    return new_dic
