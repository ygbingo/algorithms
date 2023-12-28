"""
Bellman Ford
"""
from shortest_path.graph import Graph, Edge


def print_dist(vertices, dist):
    print("graph vertices distance: ")
    for idx in range(len(vertices)):
        print(f"{0}\t\t{1}".format(vertices[idx], dist[idx]))


def bellman_ford(graph: Graph, src):
    """
    找到最短路径
    Args:
        graph: 图结构
        src: 起始节点
    """
    vertices = list(graph.vertices)
    dist = [float("inf")] * graph.V
    dist[vertices.index(src)] = 0
    for _ in range(graph.V):
        for edge in graph.graph:
            u_idx = vertices.index(edge.u)
            v_idx = vertices.index(edge.v)
            if dist[u_idx] != float("inf") and \
               dist[u_idx] + edge.w < dist[v_idx]:
                dist[v_idx] = dist[u_idx] + edge.w

    for edge in graph.graph:
        u_idx = vertices.index(edge.u)
        v_idx = vertices.index(edge.v)
        if dist[u_idx] != float("inf") and dist[u_idx] + edge.w < dist[v_idx]:
            raise Exception(msg="存在递减环")
        
    print_dist(vertices, dist)