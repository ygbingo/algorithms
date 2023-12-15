"""
链表
"""


class LinkedNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None


class DoublyLinkedNode:
    """
    双向链表
    """
    def __init__(self, x=0, pre=None):
        self.val = x
        self.pre = pre
        self.next = None


def linked_search(head: LinkedNode, k):
    while head and head.val != k:
        head = head.next
    return head

def linked_insert(node: LinkedNode, x):
    new_node = LinkedNode(x)
    new_node.next = node.next
    node.next = new_node

def linked_delete(head: LinkedNode, x):
    move = head
    while move and move.val != x:
        pre = move
        move = move.next
    pre.next = move.next
    return head
