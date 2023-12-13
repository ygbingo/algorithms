"""
归并排序
"""


def merge(A, p, q, r, reverse=False):
    """
    合并
    A[p, ..., q], A[q+1, ..., r] is sorted
    """
    n1 = q - p + 1
    n2 = r - q
    left = [0] * (n1 + 1)
    right = [0] * (n2 + 1)
    for i in range(0, n1):
        left[i] = A[p+i]
    for i in range(0, n2):
        right[i] = A[q+1+i]
    if not reverse:
        left[n1] = float('inf')
        right[n2] = float('inf')
    else:
        left[n1] = float('nan')
        right[n2] = float('nan')
    i, j = 0, 0
    for k in range(p, r+1):
        if not reverse:
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
        else:
            if left[i] >= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1


def merge_sort(A, p, r, reverse=False):
    if p < r:
        q = int((r+p) / 2)
        merge_sort(A, p, q, reverse)
        merge_sort(A, q+1, r, reverse)
        merge(A, p, q, r, reverse)


def sort(A, reverse=False):
    merge_sort(A, 0, len(A)-1, reverse)