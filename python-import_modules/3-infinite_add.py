#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    length_argv = len(argv)
    sum = 0

    if length_argv > 1:
        for i in range(1, length_argv):
            sum += int(argv[i])
    print("{}".format(sum))
