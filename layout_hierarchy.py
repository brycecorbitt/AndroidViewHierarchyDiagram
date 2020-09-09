"""
Bryce Corbitt
layout_hierarchy.py

Main script to read in an Android layout XML file and provide a detailed View hierarchy diagram.
"""
import sys
import pygraphviz as PG
from tree import android_layout_tree

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 layout_hierarchy.py /path/to/layout.xml /path/for/exported/diagram.png")
        exit(1)

    path, export_path = sys.argv[1], sys.argv[2]
    tree = None
    try:
        tree = android_layout_tree(path)
    except BaseException as e:
        print(f'Unexpected Exception while reading {path}: {e}')
        exit(1)
    nodes = [tree]

    # Set up graphviz graph, add
    A = PG.AGraph(directed=True, strict=True)
    A.node_attr['shape'] = 'box'
    A.add_node(tree.id, label=tree.name)

    while len(nodes) > 0:
        node = nodes.pop()
        for child in node.children:
            nodes.append(child)
            A.add_node(child.id, label=child.name)
            A.add_edge(node.id, child.id)

    # save the graph in dot format
    # A.write('test.dot')

    A.layout(prog='dot')
    if not export_path.endswith('.png'):
        export_path += '.png'
    A.draw(export_path)
