#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    else:
        roman = roman_string
        s = 0
        if 'IV' in roman:
            s = s + 4
            roman = roman.replace("IV", "")
        if "IX" in roman:
            s = s + 9
            roman = roman.replace("IX", "")
        if "XL" in roman:
            s = s + 40
            roman = roman.replace("XL", "")
        if "XC" in roman:
            s = s + 90
            roman = roman.replace("XC", "")
        if "CD" in roman:
            s = s + 400
            roman = roman.replace("CD", "")
        if "CM" in roman:
            s = s + 900
            roman = roman.replace("CM", "")
        for char in roman:
            if char == 'M':
                s += 1000
            if char == 'D':
                s += 500
            if char == 'C':
                s += 100
            if char == 'L':
                s += 50
            if char == 'X':
                s += 10
            if char == 'V':
                s += 5
            if char == 'I':
                s += 1
    return s
