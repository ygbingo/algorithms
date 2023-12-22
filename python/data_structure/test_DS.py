from b_tree import BTree


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