# Initially, Contributed by Neelam Yadav
# Later On, Edited by Himanshu Garg

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])