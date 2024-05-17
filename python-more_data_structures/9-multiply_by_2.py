#!/usr/bin/python3

def multiply_by_2(my_dict):
    buffer = my_dict.copy()
    for i in buffer.keys():
        buffer[i] *= 2
    return (buffer)
