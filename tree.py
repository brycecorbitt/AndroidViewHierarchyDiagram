"""
Bryce Corbitt
tree.py

Utility script to parse XML and re-format into something more presentable.
"""
import xml.etree.ElementTree as ET
from uuid import uuid4


# A class for storing formatted node diagram data
class TreeNode:
    def __init__(self, name: str, children: list):
        self.id = uuid4().int  # unique identifier to prevent
        self.name = name
        self.children = children


# Read in an XML file, extract the type and attributes of each view recursively, and cast to TreeNode
def android_layout_tree(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    def to_tree_node(xml_node: ET.Element):
        name = xml_node.tag
        attribs = xml_node.attrib.copy()
        keys = list(attribs.keys())
        for key in keys:
            if key.startswith('{'):
                new_key = key[key.index('}')+1:]
                attribs[new_key] = attribs[key]
                del attribs[key]

        if 'id' in attribs:
            name += f' → {attribs["id"]}'
        name += '\n'
        for k, v in attribs.items():
            if k != 'id':
                name += f'\n{k}="{v}"'
        children = [to_tree_node(child) for child in xml_node]
        return TreeNode(name, children)
    return to_tree_node(root)
