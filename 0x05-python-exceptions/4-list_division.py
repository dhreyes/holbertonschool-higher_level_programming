#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    quotient = 0
    for idx in range(0, list_length):
        try:
            quotient = 0
            quotient = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(quotient)
    return new_list

