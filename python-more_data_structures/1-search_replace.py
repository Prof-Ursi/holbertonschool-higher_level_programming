#!/usr/bin/python3

def search_replace(my_list, search, replace):
    buffer = my_list.copy()

    for i in range(len(buffer)):
        if buffer[i] == search:
            buffer[i] = replace
    return buffer
