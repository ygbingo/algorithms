"""
最长公共子序列(LCS: longest common subsequence)问题是给定两个序列,
求出其中最长的子序列, 该子序列可以是两个序列中任何一个序列的子序列,
但不必是连续的。
"""

RES_LCS = []
def print_lcs(b, X, i, j):
    """
    返回X和Y的一个LCS
    Args:
        b: lcs_length构建的b表
        X: X序列
        i: X.length
        j: Y.length
    """
    if i == 0 or j == 0:
        return
    if b[i-1][j-1] == "left-up":
        print_lcs(b, X, i-1, j-1)
        RES_LCS.append(X[i-1])
    elif b[i-1][j-1] == "up":
        print_lcs(b, X, i-1, j)
    else:
        print_lcs(b, X, i, j-1)

def lcs_length(X, Y):
    """
    返回X和Y的LCS的长度
    """
    m = len(X)
    n = len(Y)
    b = [[0 for x in range(n)] for y in range(m)]
    c = [[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i-1][j-1] = "left-up"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i-1][j-1] = "up"
            else:
                c[i][j] = c[i][j-1]
                b[i-1][j-1] = "left"
    return c, b

def stanford_lcs_length(X, Y):
    """
    [斯坦福课件](https://web.stanford.edu/class/cs97si/04-dynamic-programming.pdf)中描述的lcs长度代码
    """
    m, n = len(X), len(Y)
    D = [[0] * (n+1)] * (m+1)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                D[i][j] = D[i-1][j-1] + 1
            else:
                D[i][j] = max(D[i-1][j], D[i][j-1])

X = "ABCBDAB"
Y = "BDCABA"
(c, b) = lcs_length(X, Y) 
print_lcs(b, X, len(X), len(Y))
print(X)
print(Y)
print("".join(RES_LCS))

stanford_lcs(X, Y)