#!/usr/bin/python3
"""
This module provides functions to serialize a dictionary to an XML file and
deserialize an XML file back to a dictionary.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary to an XML file.
    Returns:
        bool: True if the serialization is successful.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

    return True


def deserialize_from_xml(filename):
    """
    Deserialize data from an XML file.

    Returns:
        dict: A dictionary containing the deserialized data from the XML file.
              Returns None if the file is not found or if there is an error
              parsing the XML.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    data_dict = {}
    for child in root:
        data_dict[child.tag] = child.text

    return data_dict
