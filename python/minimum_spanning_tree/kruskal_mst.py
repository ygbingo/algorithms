"""
Kruskal最小生成树
1. Sort all the edges in non-decreasing order of their weight. 
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. 
    If the cycle is not formed, include this edge. Else, discard it. 
3. Repeat step#2 until there are (V-1) edges in the spanning tree.
"""
from collections import defaultdict
from model import Edge


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # 端点数量
        self.nodes = set()  # 端点集合
        self.graph = []

    def add_edge(self, edge: Edge):
        self.graph.append(edge)
        self.nodes.add(edge.u)
        self.nodes.add(edge.v)

    def find_root(self, roots, u):
        """
        找到u所在树的根
        """
        if roots[u] != u:
            self.find_root(roots, roots[u])
        return roots[u]
    
    def union(self, roots, ru, rv):
        """
        把ru和rv为根的树合并为一个树
        """
        roots[ru] = rv
        return

    def kruskal_mst(self):
        self.graph = sorted(self.graph, key=lambda edge: edge.w)

        results = []
        roots = defaultdict()  # 构建森林
        for node in self.nodes:
            roots[node] = node
        i = 0  # 遍历graph的索引
        while len(results) < self.V - 1:
            edge = self.graph[i]
            ru = self.find_root(roots, edge.u)
            rv = self.find_root(roots, edge.v)
            if ru != rv:
                results.append(edge)
                self.union(roots, ru, rv)
            i += 1
            if i > len(self.graph): break
        return results



# Driver code 
if __name__ == '__main__': 
    g = Graph(4) 
    g.add_edge(Edge(0, 1, 10))
    g.add_edge(Edge(0, 2, 6))
    g.add_edge(Edge(0, 3, 5))
    g.add_edge(Edge(1, 3, 15))
    g.add_edge(Edge(2, 3, 4))
  
    # Function call 
    results = g.kruskal_mst()
    print(results)