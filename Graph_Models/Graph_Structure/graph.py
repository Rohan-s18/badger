"""
this is the main code to make a graph using badger
"""


# importing inner workings
from Node_Structure import heterogenous_node, homogeous_node
from Edge_Structure import *


# other imports
import numpy as np



# class for a graph structure
class Graph:

    # initialization function
    def __init__(self, homogenous_nodes=True, labeled_edges=False, directed=False) -> None:

        self.homogeneity = homogenous_nodes
        self.labeled_edges = labeled_edges
        self.nodes = []
        self.edges = []
        self.directed = directed
        self.A = None

    
    # function to add a vertex
    def add_vertex(self, name, properties=None):

        if(self.homogeneity == False):
            self.nodes.append(heterogenous_node.HeterogenousNode(label=name, properties=properties))
        else:
            self.nodes.append(homogeous_node.HomogenousNode(label=name))

        
    # function to add an edge



