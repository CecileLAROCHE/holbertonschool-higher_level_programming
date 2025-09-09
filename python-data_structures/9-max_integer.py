#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        biggest = my_list[0]
        for nb in my_list:
            if nb > biggest:
                biggest = nb
    return biggest
