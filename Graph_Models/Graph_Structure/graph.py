"""
this is the main code to make a graph using badger
"""


# importing inner workings
from Node_Structure import heterogenous_node, homogeous_node
from Edge_Structure import heterogenous_edge, homogeous_edge


# other imports
import numpy as np



# class for a graph structure
class Graph:


    # initialization function
    def __init__(self, homogenous_nodes=True, homogenous_edges=True, directed=False) -> None:

        self.node_homogeneity = homogenous_nodes
        self.edge_homogeneity = homogenous_edges
        self.nodes = []
        self.edges = []
        self.directed = directed
        self.A = None               # (decide between tf, pytorch ot numpy)

    
    # function to add a node
    def add_node(self, name, properties=None):

        if(self.node_homogeneity == False):
            self.nodes.append(heterogenous_node.HeterogenousNode(label=name, properties=properties))
        else:
            self.nodes.append(homogeous_node.HomogenousNode(label=name))

        # resize A (decide between tf, pytorch ot numpy)
            

    # function to remove a node
    def remove_node(self, name):

        i = -1
        for node in self.nodes:
            if node.name == name:
                i = self.nodes.index(node)
                self.nodes.remove(node)

        # remove A[i] depending on implementation
                

        
    # function to add an edge
    def add_edge(self, node_a, node_b, directed=False, name=None, properties=None):

        if(self.edge_homogeneity == False):
            self.edges.append(heterogenous_edge.HeterogenousEdge(label=name,node_1=node_a,node_2=node_b, directed=directed,properties=properties))
        else:
            self.edges.append(homogeous_edge.HomogenousEdge(label=name, node_1=node_a, node_2=node_b, directed=directed))

        # add edge to A (decide between tf, pytorch or numpy)
            


    # function to remove an edge
    def remove_edge(self, vertex_a, vertex_b):

        for edge in self.edges: 
            if(edge.node_1 == vertex_a and edge.node_2 == vertex_b):
                self.edges.remove(edge)

        # remove entry from A (decision of A pending)



