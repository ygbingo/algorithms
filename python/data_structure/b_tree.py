"""
B树
"""


class BTreeNode:
    def __init__(self, t, leaf):
        self.t = t  # 最小度，每个节点的key的数量<=2t-1
        self.keys = [0] * (2 * t - 1)  # 关键字
        self.childs = [None] * (2 * t)
        self.n = 0  # 当前key的数量
        self.leaf = leaf

    def split_child(self, i, child):
        """
        拆分已满子节点：
        1. 构建新节点保存child的后半部分内容；
        2. 把新节点插入到父节点对应位置；
        3. 把child中间值插入到父节点的keys中
        Args:
            i: child在父节点中的索引
            child: 子节点
        """
        new_node = BTreeNode(child.t, child.leaf)
        new_node.n = self.t - 1  # 因为child.leaf已满，长度为2t-1，拆分的节点长度为满节点的一半t-1
        for j in range(self.t - 1):
            new_node.keys[j] = child.keys[j + self.t]
        if not child.leaf:
            for j in range(self.t):
                new_node.childs[j] = child.childs[j]
        child.n = self.t - 1
        for j in range(self.n, i, -1):
            self.childs[j + 1] = self.childs[j]
        self.childs[i + 1] = new_node
        for j in range(self.n - 1, i - 1, -1):
            self.keys[j+1] = self.keys[j]
        self.keys[i] = child.keys[self.t - 1]
        self.n += 1

    def insert_not_full(self, k):
        """
        把k插入到未满的节点中
        """
        i = self.n - 1
        if self.leaf:
            while i >= 0 and self.keys[i] > k:
                self.keys[i+1] = self.keys[i]
                i -= 1
            self.keys[i+1] = k
            self.n += 1
        else:
            while i >= 0 and self.keys[i] > k:
                i -= 1
            if self.childs[i+1].n == 2 * self.t - 1:
                self.split_child(i+1, self.childs[i+1])
                if self.keys[i+1] < k: i += 1
            self.childs[i+1].insert_not_full(k)

    def search(self, k):
        i = 0
        while i < self.n and self.keys[i] < k:
            i += 1
        if i < self.n and self.keys[i] == k:
            return self
        if self.leaf: return None
        return self.childs[i].search(k)
    
    def traverse(self):
        """
        遍历当前节点为根的B树
        """
        for i in range(self.n):
            print(self.keys[i])
            if not self.leaf:
                self.childs[i].traverse()
        if not self.leaf:
            self.childs[i+1].traverse()
    

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = None
        self.MAX_VAL = 2 * t - 1

    def traverse(self):
        if self.root:
            return self.root.traverse()
        return None

    def search(self, k):
        """
        返回值为k的节点
        """
        if not self.root: return None
        return self.root.search(k)

    def insert(self, k):
        """
        插入k
        """
        if not self.root:
            self.root = BTreeNode(self.t, True)
            self.root.keys[0] = k
            self.root.n = 1
        else:
            if self.root.n == 2 * self.t - 1:
                # 根已满，需要拆分后插入
                new_root = BTreeNode(self.t, False)
                new_root.childs[0] = self.root
                new_root.split_child(0, new_root.childs[0])
                if new_root.keys[0] > k:
                    new_root.childs[0].insert_not_full(k)
                else:
                    new_root.childs[1].insert_not_full(k)
                self.root = new_root
            else:
                self.root.insert_not_full(k)