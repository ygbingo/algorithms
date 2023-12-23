"""
图(G = <V, E>, graph, vertices, edges)：广度优先搜索(BFS)，深度优先搜索(DFS)
"""
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start):
        """
        深度优先搜索
        Args:
            start: 起始节点
        """
        visited = [start]
        next_visited = self.graph[start]
        while next_visited:
            node = next_visited.pop(-1)
            if node in visited:
                continue
            visited.append(node)
            for _v in self.graph[node]:
                if _v not in visited:
                    next_visited.extend(self.graph[node])
        return visited


    def bfs(self, start):
        """
        广度优先搜索
        """
        visitied = [False] * (max(self.graph) + 1)
        queue = [start]
        visitied[start] = True
        result = []

        while queue:
            v = queue.pop(0)
            result.append(v)
            print(v)
            print(self.graph[v])
            for _v in self.graph[v]:
                if not visitied[_v]:
                    visitied[_v] = True
                    queue.append(_v)

        return result


if __name__=='__main__':
    g = Graph()
    g.add_edge(2, 0)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(0, 1)
    g.add_edge(3, 3)
    g.add_edge(1, 3)
    print(g.dfs(2))