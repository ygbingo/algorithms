"""
红黑树:
1. 每个节点颜色为红色或黑色
2. 根节点为黑色
3. 每个叶节点(NIL)是黑色的
4. 如果一个节点是红色，则它的两个子节点是黑色的
5. 对每个节点，其到所有后代叶节点的简单路径上，均包含相同数量的黑色节点(不包含本身)
"""
from tree import Tree
from node import RB_Node as Node
from node import Color


class RedBlackTree(Tree):
    def __init__(self, val):
        self.NIL = Node(None)
        self.root = Node(val, nil=self.NIL)
        self.black_hight = 1  # 黑高: 根节点到NIL节点黑色节点的数量

    def rb_delete(self, z: Node):
        """
        红黑树删除节点z
        """
        y = z
        y_ori_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_ori_color = y.color
            x = y.right
            if y.parent == x:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_ori_color == Color.BLACK:
            self.rb_delete_fixup(x)

    def rb_delete_fixup(self, x: Node):
        """ 删除节点的自适应方法 """
        while x != self.NIL and x.color == Color.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                elif w.right.color == Color.RED:
                    w.left.color = Color.BLACK
                    w.color = Color.RED
                    self.right_rotate(w)
                    w = x.parent.right
                w.color = x.parent.color
                x.parent.color = Color.BLACK
                w.right.color = Color.BLACK
                self.left_rotate(x.parent)
                x = self.root
            else:
                w = x.parent.left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                elif w.left.color == Color.RED:
                    w.right.color = Color.BLACK
                    w.color = Color.RED
                    self.left_rotate(w)
                    w = x.parent.left
                w.color = x.parent.color
                x.parent.color = Color.BLACK
                w.left.color = Color.BLACK
                self.right_rotate(x.parent)
                x = self.root
        x.color = Color.BLACK

    def rb_transplant(self, u, v):
        """
        v节点代替u节点
        """
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def rb_insert(self, z: Node):
        """
        向红黑树中插入新的节点z
        """
        y = self.NIL
        x = self.root
        while x != self.NIL:
            y = x
            if z.val < x.val:
                x = x.left
            else: x = x.right
        z.parent = y
        if y == self.NIL:
            self.root = z
        elif z.val < y.val:
            y.left = z
        else: y.right = z
        z.left = self.NIL
        z.right = self.NIL
        z.color = Color.RED
        self.rb_insert_fixup(z)

    def rb_insert_fixup(self, z: Node):
        """
        保持红黑树性质
        """
        while z.parent.color == Color.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                elif z == z.parent.right:
                    z = z.parent
                    self.left_rotate(z)
                z.parent.color = Color.BLACK
                z.parent.parent.color = Color.RED
                self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                elif z == z.parent.left:
                    z = z.parent
                    self.right_rotate(z)
                z.parent.color = Color.BLACK
                z.parent.parent.color = Color.RED
                self.left_rotate(z.parent.parent)
        self.root.color = Color.BLACK

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
