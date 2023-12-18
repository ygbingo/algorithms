"""
树
"""
from node import Node

class Tree:
    def __init__(self, sequence: list):
        self.root = self.build_bst_iter(sequence)
        self.tree_walk_lst = []

    def search(self, val):
        """
        查找节点为val的节点
        Args:
            val: 查找的目标值
        """
        node = self.root
        while node and node.val != val:
            if node.val < val:
                node = node.right
            else:
                node = node.left
        return node

    def predecessor(self, node: Node):
        """
        查找当前节点的前驱
        """
        if node.left:
            return self.maximum(node.left)
        parent = node.parent
        while parent and node == parent.left:
            node = parent
            parent = parent.parent
        return parent

    def successor(self, node: Node):
        """
        查找当前节点的后继
        Args:
            node: 要查找的节点
        """
        if node.right:
            return self.minimum(node.right)
        parent = node.parent
        while parent and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    def maximum(self, node=None):
        """
        找到最大的节点
        """
        if not node:
            node = self.root
        while node.right:
            node = node.right
        return node

    def minimum(self, node=None):
        """
        找到最小的节点
        """
        if not node:
            node = self.root
        while node.left:
            node = node.left
        return node

    def transplant(self, his_node, new_node):
        """
        替换子树
        Args:
            his_node: 需要被删掉的节点
            new_node: 用来作替换的节点
        """
        if his_node.parent is None:
            self.root = new_node
        elif his_node == his_node.parent.left:
            his_node.parent.left = new_node
        else:
            his_node.parent.right = new_node
        if not new_node:
            new_node.parent = his_node.parent

    def delete(self, val, root):
        """
        删除节点为val的值
        Args:
            val: 要删除的val
            root: 当前子树的根节点
        """
        if root is None: return None
        if val < root.val:
            root.left = self.delete(val, root.left)
        elif val > root.val:
            root.right = self.delete(val, root.right)
        else:
            if not root.left:
                self.transplant(root, root.right)
            elif not root.right:
                self.transplant(root, root.left)
            else:
                node = self.minimum(root.right)
                if node.parent != root:
                    self.transplant(node, node.right)
                    node.right = root.right
                    node.right.parent = node
                self.transplant(root, node)
                node.left = root.left
                node.left.parent = node

    def build_bst_iter(self, sequence: list):
        """
        构建二叉搜索树
        Args:
            sequence: 输入的序列
        """
        root = None
        for val in sequence:
            root = self.insert(root, val)
        return root

    def insert(self, root, val):
        """
        插入val
        Args:
            root: 当前节点
            val: 要插入的值
        """
        if not root:
            return Node(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
            root.left.parent = root
        else:
            root.right = self.insert(root.right, val)
            root.right.parent = root
        return root

    def inorder_tree_walk(self, node):
        """
        中序遍历: 左->中->右
        """
        if node:
            self.inorder_tree_walk(node.left)
            self.tree_walk_lst.append(node.val)
            self.inorder_tree_walk(node.right)    

    def first_tree_walk(self, node):
        """
        先序遍历: 中->前->后
        """    
        if node:
            self.tree_walk_lst.append(node.val)
            self.first_tree_walk(node.left)
            self.first_tree_walk(node.right)

    def behind_tree_walk(self, node):
        """
        先序遍历: 中->前->后
        """    
        if node:
            self.behind_tree_walk(node.left)
            self.behind_tree_walk(node.right)
            self.tree_walk_lst.append(node.val)



