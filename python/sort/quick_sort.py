"""
快速排序
最坏: O(n2)
平均期望: O(nlgn)
"""


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if (A[j] <= x if not rev else A[j] > x):
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def sort(A, reverse=False):
    global rev
    rev = reverse
    quick_sort(A, 0, len(A)-1)