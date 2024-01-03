class Color:
    BLACK = 'black'
    RED = 'red'


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Treap_Node:
    def __init__(self, val):
        self.val = val
        self.priority = 0  # 树堆中节点的权重
        self.left = None
        self.right = None
        self.parent = None


class RB_Node:
    def __init__(self, val, nil=None, color=Color.BLACK):
        self.val = val
        self.color = color  # 红黑树属性
        self.left = nil
        self.right = nil
        self.parent = nil


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next