"""
Python Module for Creating Heterogenous Nodes in graphs
"""


class HeterogenousEdge:

    def __init__(self, label, node_1, node_2, directed=False, properties=None) -> None:
        self.label = label
        self.directed = directed
        if directed:
            self.to_label = node_1
            self.to_label = node_2
        else:
            self.node_1 = node_1
            self.node_2 = node_2
        self.properties = properties
