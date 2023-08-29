#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    div_list = [0] * list_length
    for index in range(list_length):
        try:
            div_list[index] = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
    return (div_list)
