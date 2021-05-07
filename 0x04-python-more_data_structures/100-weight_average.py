#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    average = 0
    total = 0
    for key, value in my_list:
        average += key * value
        total +=  value
    return average/total
