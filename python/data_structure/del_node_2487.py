"""
2487: 从链表中移除节点
https://leetcode.cn/problems/remove-nodes-from-linked-list/
"""
from typing import Optional, List
from node import ListNode


def build_nodes(nodes: Optional[int]) -> ListNode:
    if len(nodes) < 1: return None
    head = ListNode(nodes[0])
    tail = head
    for node in nodes[1:]:
        tail.next = ListNode(node)
        tail = tail.next
    return head

def show_nodes(head: ListNode) -> List:
    nodes = []
    while head:
        nodes.append(head.val)
        head = head.next
    return nodes

def remove_nodes(head: Optional[ListNode]) -> Optional[ListNode]:
    stack = []
    while head:
        stack.append(head)
        head = head.next
    while stack:
        if head is None or stack[-1].val >= head.val:
            stack[-1].next = head
            head = stack[-1]
        stack.pop()
    return head