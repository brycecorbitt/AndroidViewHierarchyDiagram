# Android View Hierarchy Diagram Generator
A simple tool that uses Graphviz to generate View Hierarchy diagrams from Android layout resources in the form of XML files.
###### NOTE: This code is UGLY and hacked together in a few hours. Maybe I'll make it look more presentable in the future.
## Setup
This program requires Python3 to run. It should work on anything >= Python3.4, but has only been run on Python3.6. 
- Install Graphviz for your OS at the following URL: http://www.graphviz.org/download/

- Install python dependencies (currently only pygraphviz):
    ```
    pip3 install -r requirements.txt
    ```

- Run `layout_hierarchy.py` with the path to your layout XML file and the save location of the exported diagram.
    ```
    python3 layout_hierarchy.py /path/to/layout.xml /path/for/exported/diagram.png
    ```

After running successfully for an app like this:
![Test App](https://i.imgur.com/iHn45kh.png)

You should get a resulting diagram that looks like this:
![Test Diagram](https://i.imgur.com/W6ckDEg.png)
