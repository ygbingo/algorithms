from b_tree import BTree
from graph import Graph
from node import ListNode
from del_node_2487 import remove_nodes, build_nodes, show_nodes


def test_2487():
    heads = [5,2,13,3,8]
    head = build_nodes(heads)
    assert show_nodes(remove_nodes(head)) == [13, 8]

def test_BFS():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    assert g.bfs(2) == [2, 0, 3, 1]

def test_DFS():
    g = Graph()
    g.add_edge(2, 0)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(0, 1)
    g.add_edge(3, 3)
    g.add_edge(1, 3)
    assert g.dfs(2) == [2, 0, 1, 3]

def test_BTree():
    t = BTree(3)  # A B-Tree with minimum degree 3
    t.insert(10)
    t.insert(20)
    t.insert(5)
    t.insert(6)
    t.insert(12)
    t.insert(30)
    t.insert(7)
    t.insert(17)
 
    print("Traversal of the constructed tree is ", end = ' ')
    t.traverse()
    print()
    assert t.search(6) != None
    assert t.search(15) is None