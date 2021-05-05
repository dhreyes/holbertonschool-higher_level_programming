#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = [0, 0]
    for idx in range(0, 2):
        try:
            result[idx] += tuple_a[idx]
        except:
            result[idx] += 0
        try:
            result[idx] += tuple_b[idx]
        except:
            result[idx] += 0
    tup_result = tuple(result)
    return tup_result
