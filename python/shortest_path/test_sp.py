from shortest_path.graph import Edge, Graph
from shortest_path.bellman_ford import bellman_ford


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