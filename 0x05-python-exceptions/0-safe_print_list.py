#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for a in range(0, x):
            print(my_list[a], end="")
            counter += 1
    except TypeError:
        pass
    except IndexError:
        pass
    finally:
        print()
        return (counter)
