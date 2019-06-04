import networkx as nx
import metis
import math
import pygraphviz as pgv

def graphPartition(G, clusterSize):
    numClusters = math.ceil(len(G)/float(clusterSize)) # heuristic for # of clusters given approximately equal cluster size
    print numClusters
    (edgecuts, parts) = metis.part_graph(G, int(numClusters)) # k-way cut algorithm
    colors = ['red', 'blue', 'green', 'orange', 'yellow', 'purple', 'black', 'maroon', 'brown', 'indigo', 'cyan']
    for i, p in enumerate(parts):
        #print i, p
        G.node[i]['color'] = colors[p]
    nx.drawing.nx_pydot.write_dot(G, 'example.dot')  # writes graph partition into dot file format
    result = pgv.AGraph('example.dot')  # load dot format representation of graph to create visualization
    result.node_attr.update(shape='circle')
    result.node_attr.update(label=' ')
    result.node_attr.update(style='filled')
    result.layout()  # default layout
    result.draw('example.svg')  # writes visualization as svg file
    print("Wrote example.svg")


graphPartition(nx.circular_ladder_graph(25), 10)
