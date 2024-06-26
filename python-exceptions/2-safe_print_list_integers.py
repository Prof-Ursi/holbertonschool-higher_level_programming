#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    int_printed = 0
    for i in range(x):
        try:
            if type(my_list[i]) is int:
                print('{:d}'.format(my_list[i]), end="")
                int_printed += 1
        except (ValueError, TypeError):
            continue
    print("")
    return int_printed
