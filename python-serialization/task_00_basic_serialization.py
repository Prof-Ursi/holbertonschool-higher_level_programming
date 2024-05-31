#!/usr/bin/env python3
"""
This module defines two functions.
The first one saves a python object into a JSON file,
and the second loads a JSON formatted object from a file.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Saves the given Python object to a JSON file.

    Args :
        - data (dict) : A Python Dictionary with data to be stored
        in the JSON file
        - filename (str) : The filename of the output JSON file.
    """
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load a JSON-formatted object from a file.

    Args :
        filename (str) : The filename of the input JSON file.

    Returns :
        the deserialized json file storing the data.
    """
    with open(filename, "r") as file:
        return json.load(file)
