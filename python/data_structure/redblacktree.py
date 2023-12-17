"""
红黑树:
1. 每个节点颜色为红色或黑色
2. 根节点为黑色
3. 每个叶节点(NIL)是黑色的
4. 如果一个节点是红色，则它的两个子节点是黑色的
5. 对每个节点，其到所有后代叶节点的简单路径上，均包含相同数量的黑色节点(不包含本身)
"""


class Color:
    BLACK = 'black'
    RED = 'red'


class Node:
    def __init__(self, val, nil=None, color=Color.BLACK):
        self.val = val
        self.color = color
        self.left = nil
        self.right = nil
        self.parent = nil


class RedBlackTree:
    def __init__(self, val):
        self.NIL = Node(None)
        self.root = Node(val, nil=self.NIL)

    def left_rotate(self, node):
        """
        左旋
        """
        y = node.right
        node.right = y.left
        if y.left != self.NIL:
            y.left.parent = node
        y.parent = node.parent
        if node.parent == self.NIL:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def right_rotate(self, node):
        """
        右旋
        """
        y = node.left
        node.left = y.right
        if y.right != self.NIL:
            y.right.parent = node
        y.parent = node.parent
        if node.parent == self.NIL:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y
