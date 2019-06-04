import networkx as nx
import metis
import math
import pydot
import pygraphviz as pgv

def graphPartition(G, clusterSize):
    numPartitions = math.ceil(G.size()/float(clusterSize)) # heuristic for # of clusters given approximately equal cluster size
    (edgecuts, parts) = metis.part_graph(G, int(numPartitions)) # k-way cut algorithm
    colors = ['red', 'blue', 'green', 'orange', 'yellow', 'purple', 'black']
    for i, p in enumerate(parts):
        G.node[i]['color'] = colors[p]
    nx.drawing.nx_pydot.write_dot(G, 'example.dot')  # writes graph partition into dot file format
    result = pgv.AGraph('example.dot')  # load dot format representation of graph to create visualization
    result.layout()  # default layout
    result.draw('example.svg')  # writes visualization as svg file
    print("Wrote example.svg")


graphPartition(metis.example_networkx(), 6)
