#!/usr/bin/env python3
"""
This module defines two functions.
The first one serializes a python dictionary to XML format,
and the second deserializes a XML file into a python dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to XML format and write it to the specified file.

    Args:
        dictionary (dict): The dictionary to be serialized.
        filename (str): The filename to save the XML data.
     """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from the specified file and return as a dictionary.

    Args:
        filename (str): The filename containing XML data.

    Returns:
        dict: The deserialized dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    deserialized_data = {}
    for child in root:
        deserialized_data[child.tag] = child.text
    return deserialized_data
