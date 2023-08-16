#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    elif not a_dictionary:
        return None
    else:
        for key in a_dictionary:
            b_val = a_dictionary[key]
            break
        for key, value in a_dictionary.items():
            if value > b_val:
                b_val = value
                b_key = key
        return b_key
