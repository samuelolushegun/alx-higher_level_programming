#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def replac(x):
        if x == search:
            return replace
        else:
            return x
    n_list = [replac(elmt) for elmt in my_list]
    return n_list
