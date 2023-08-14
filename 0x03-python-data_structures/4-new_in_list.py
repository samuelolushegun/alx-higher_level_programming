#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    n_list = []
    for i in my_list:
        n_list.append(i)
    if idx >= 0 and idx < len(n_list):
        n_list[idx] = element
    return n_list
