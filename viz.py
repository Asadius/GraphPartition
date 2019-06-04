import networkx as nx
import metis
import math
import pydot
import pygraphviz as pgv

def graphPartition(G, clusterSize):
    numPartitions = int(math.ceil(G.size()/float(clusterSize)))
    (edgecuts, parts) = metis.part_graph(G, numPartitions, objtype='vol')
    colors = ['red', 'blue', 'green', 'orange', 'yellow', 'purple', 'black']
    for i, p in enumerate(parts):
        G.node[i]['color'] = colors[p]
    nx.drawing.nx_pydot.write_dot(G, 'example.dot')
    B = pgv.AGraph('example.dot')  # create a new graph from file
    B.layout()  # layout with default (neato)
    B.draw('example.svg')  # draw png
    print("Wrote simple.png")


graphPartition(metis.example_networkx(), 6)
