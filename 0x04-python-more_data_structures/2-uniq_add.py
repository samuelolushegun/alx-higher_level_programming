#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = 0
    check_list = []
    for i in my_list:
        if i not in check_list:
            check_list.append(i)
            s = s + i
    return s
