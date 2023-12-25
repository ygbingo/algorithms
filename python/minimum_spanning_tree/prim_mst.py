"""
Prim算法
"""
from model import Edge
import heapq
from heapq import heappush


class Graph:
    def __init__(self, vertices):
        """
        vertices: 关系矩阵，值代表每两个节点之间的权重
        """
        self.V = vertices
        self.graph = [[0] * vertices] * vertices

    def find_next_visit(self, visitied):
        """
        找到下一个访问的节点
        Args:
            visited: 已经访问的节点
        """
        heapq.heapify(visitied)
        min_weight = float("inf")
        next_visit = self.V - 1  # 假设访问最后一个节点
        for visit in visitied:
            for i in range(self.V):
                if i not in visitied and self.graph[visit][i] < min_weight:
                    next_visit = Edge(visit, i, self.graph[visit][i])
                    min_weight = self.graph[visit][i]
        return next_visit

    def prim_mst(self):
        # Prim
        weights = 0
        visitied = [0]
        result = []
        while len(visitied) < self.V:
            next_visit = self.find_next_visit(visitied)
            visitied.append(next_visit.v)
            result.append(next_visit)
            weights += next_visit.w
        return result, weights
 
 
if __name__ == '__main__':
    g = Graph(9)
    g.graph = [[0, 4, float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 8, float("inf")],
               [4, 0, 8, float("inf"), float("inf"), float("inf"), float("inf"), 11, float("inf")],
               [float("inf"), 8, 7, float("inf"), float("inf"), 4, float("inf"), float("inf"), 2],
               [float("inf"), float("inf"), 7, 0, 9, 14, float("inf"), float("inf"), float("inf")],
               [float("inf"), float("inf"), float("inf"), 9, 0, 10, float("inf"), float("inf"), float("inf")],
               [float("inf"), float("inf"), 4, 14, 10, 0, float("inf"), float("inf"), float("inf")],
               [float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 2, 0, 1, 6],
               [8, 11, float("inf"), float("inf"), float("inf"), float("inf"), 1, 0, 7],
               [float("inf"), float("inf"), 2, float("inf"), float("inf"), float("inf"), 6, 7, 0]]
 
    result, weights = g.prim_mst()
    print(result)
    print(weights)