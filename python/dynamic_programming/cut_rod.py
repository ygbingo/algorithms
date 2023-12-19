""" 
钢条问题（Cutting Rod Problem）是动态规划的一个经典问题。
给定一段长度为n的钢条和一个价格表，其中p[i]表示长度为i的钢条的售价。
求切割钢条方案，使得销售收益最大。
"""


def bottom_up_cut_rod(p, n):
    """
    自底向上
    """
    r = [0] * (n+1)
    s = [0] * (n+1)
    for j in range(1, n+1):
        q = float('-inf')
        for i in range(0, j):
            if q < p[i] + r[j-(i+1)]:
                q = p[i] + r[j-(i+1)]
                s[j] = i+1
        r[j] = q
    return r, s

def memoized_cut_rod(p, n):
    """
    自顶向下
    """
    r = []
    for i in range(0, n+1):
        r.append(float('-inf'))
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    """ 
    自顶向下
    """
    if r[n-1] > 0:
        return r[n-1]
    if n == 0: 
        q = 0
    else:
        q = float('-inf')
        for i in range(0, n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n-(i+1), r))
    r[n-1] = q
    return q