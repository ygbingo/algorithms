"""
冒泡排序: 时间复杂度O(n2)
"""


def sort(A, reverse=False):
    for i in range(0, len(A)-1):
        for j in range(len(A)-1, i, -1):
            if not reverse:
                if A[j] < A[j-1]:
                    A[j], A[j-1] = A[j-1], A[j]
            else:
                if A[j] >= A[j-1]:
                    A[j], A[j-1] = A[j-1], A[j]