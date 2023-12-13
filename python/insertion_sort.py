"""
插入排序
"""

 
def sort(A: list, reverse=False):
    j = 1
    for j in range(len(A)):
        key = A[j]
        i = j - 1
        if not reverse:
            while i >= 0 and A[i] > key:
                A[i+1] = A[i]
                i = i - 1
        else:
            while i >= 0 and A[i] < key:
                A[i+1] = A[i]
                i = i - 1
        A[i+1] = key
