"""
定义一个带权重的图类型
"""


class Edge:
    def __init__(self, u, v, w):
        """ u ---w---> v   """
        self.u = u
        self.v = v
        self.w = w

class Graph:
    def __init__(self, V):
        self.V = V  # 节点数量
        self.vertices = set()
        self.graph = []

    def add_edge(self, edge: list):
        self.graph.append(edge)
        self.vertices.add(edge.u)
        self.vertices.add(edge.v)