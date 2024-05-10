#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for hidden_name in dir(hidden_4):
        if hidden_name[0] != "_":
            print(hidden_name)
