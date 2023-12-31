from shortest_path.graph import Edge, Graph
from shortest_path.bellman_ford import bellman_ford
from shortest_path.dijkstra import dijkstra


def test_bellman_ford():
    g = Graph(5)
    g.add_edge(Edge(0, 1, -1))
    g.add_edge(Edge(0, 2, 4))
    g.add_edge(Edge(1, 2, 3))
    g.add_edge(Edge(1, 3, 2))
    g.add_edge(Edge(1, 4, 2))
    g.add_edge(Edge(3, 2, 5))
    g.add_edge(Edge(3, 1, 1))
    g.add_edge(Edge(4, 3, -3))
 
    # function call
    bellman_ford(g, 0)


def test_dijkstra():
    """ 算法书中有向边的举例 """
    graph = Graph(5)
    graph.add_edge(Edge("s", "y", 5))
    graph.add_edge(Edge("s", "t", 10))
    graph.add_edge(Edge("t", "x", 1))
    graph.add_edge(Edge("y", "t", 3))
    graph.add_edge(Edge("t", "y", 2))
    graph.add_edge(Edge("y", "x", 9))
    graph.add_edge(Edge("y", "z", 2))
    graph.add_edge(Edge("x", "z", 4))
    graph.add_edge(Edge("z", "x", 6))
    graph.add_edge(Edge("z", "s", 7))