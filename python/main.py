# from sort.insertion_sort import sort
# from sort.merge_sort import sort
# from sort.bubble_sort import sort
from sort.quick_sort import sort
# from sort.heap_sort import sort
from python.problems.find_maximum_subarray import find_maximum_subarray
from data_structure.tree import Tree
from data_structure.node import Node as TreeNode
from data_structure.graph import Graph 
from dynamic_programming.cut_rod import memoized_cut_rod, bottom_up_cut_rod
from dynamic_programming.lcs import lcs_length, print_lcs, RES_LCS


print("\n------------ 图 -----------")
edge_lst = [(2, 0), (0, 2), (1, 2), (2, 3), (3, 4), (4, 6), (4, 5), (0, 1), (3, 3), (1, 3)]
print("连通点集合: ", edge_lst)
g = Graph()
for edge0, edge1 in edge_lst:
    g.add_edge(edge0, edge1)
print("从2开始广度优先搜索结果: ", g.bfs(2))
print("从2开始深度优先搜索结果: ", g.dfs(2))


print("\n------- 最长公共子串 --------")
X = "ABCBDAB"
Y = "BDCABA"
(c, b) = lcs_length(X, Y) 
print_lcs(b, X, len(X), len(Y))
print(f"字符串\"{X}\"和字符串\"{Y}\"的最长公共子串为:")
print("".join(RES_LCS))

print("\n------- 动态规划：钢条切割问题 -------")
n = 5
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print("钢条价格表：", p)
r, s = bottom_up_cut_rod(p, n)
print(f"切割长度为{n}, 最大收益为{r[-1]}")
lst = []
while n > 0:
    lst.append(s[n])
    n = n-s[n]
print(f"切割长度为: {lst}")

print("\n-------- 二叉搜索树 ---------")
sequence = [6, 5, 2, 5, 8, 7]
tree = Tree(sequence)
node = tree.root
tree.inorder_tree_walk(node)
print("中序遍历: ", tree.tree_walk_lst)
tree.tree_walk_lst.clear()
node = tree.root
tree.first_tree_walk(node)
print("先序遍历: ", tree.tree_walk_lst)
tree.tree_walk_lst.clear()
node = tree.root
tree.behind_tree_walk(node)
print("后序遍历: ", tree.tree_walk_lst)

print("\n---------- 排序问题 ---------")
A = [2, 3, 4, 1, 6, 8, 9, 0]
print("before sort: ")
print(A)

print("after sort: ")
sort(A)
print(A)

print("after reverse sort: ")
sort(A, reverse=True)
print(A)

print("\n--------- 最大连续子数组问题 ----------")

A = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
B = A.copy()
print("原始股票价格：\t", A)
for i in range(len(A)-1, 0, -1):
    A[i] = A[i] - A[i-1]
A[0] = 0
print("价格变化：\t", A)
low, high, res = find_maximum_subarray(A, 0, len(A)-1)
print("第{}天[{}]买入, 第{}天[{}]卖出, 收益最高, 为：{}".format(low, B[low-1], high+1, B[high], res))