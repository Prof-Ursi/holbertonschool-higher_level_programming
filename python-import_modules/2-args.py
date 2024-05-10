#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length_argv = len(argv)
    if length_argv == 1:
        print("0 arguments.")
    elif length_argv == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(length_argv - 1))
    for i in range(1, length_argv):
        print("{}: {}".format(i, argv[i]))
