import pprint
import xml.dom.minidom
from xml.dom.minidom import Node, parse
import random

filename = "Blank_US_Map.svg"
colors = [
        "#fff6c9",
        "#c8e8c7",
        "#a4deab",
        "#8scc9f",
        "#499e8d",
        ]

def style_string(color):
    """style_string returns a style string to fill in a path"""
    return "fill:{0};stroke:#ffffff;stroke-opacity:1;stroke-width:0.75;stroke-miterlimit:4;stroke-dasharray:none".format(color)

doc = parse(filename)

with open("stateborders.txt") as f:
    #stateBorders = [line[:2] for line in f]
    stateBorders = {}
    for line in f:
        stateBorders[line[:2]] = line[6:].split(",")




print stateBorders
for node in doc.getElementsByTagName("path"):
    pathId = node.getAttribute("id")
    if pathId in stateBorders:
        #print pathId , "should be colored"

        randomNumber = random.randrange(0,len(colors))
        node.setAttribute("style", style_string(colors[randomNumber]))


with open("newMap.svg", "w") as f:
    f.write(doc.toxml())

print "Done"
