#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = sorted(a_dictionary)
    dico = dict()
    for key in a:
        print(f"{key}: {a_dictionary[key]}")
