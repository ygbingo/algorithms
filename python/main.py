# from sort.insertion_sort import sort
# from sort.merge_sort import sort
# from sort.bubble_sort import sort
from sort.quick_sort import sort
# from sort.heap_sort import sort
from find_maximum_subarray import find_maximum_subarray



print("---------- 排序问题 ---------")

A = [2, 3, 4, 1, 6, 8, 9, 0]
print("before sort: ")
print(A)

print("after sort: ")
sort(A)
print(A)

print("after reverse sort: ")
sort(A, reverse=True)
print(A)

print("--------- 最大连续子数组问题 ----------")

A = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
B = A.copy()
print("原始股票价格：\t", A)
for i in range(len(A)-1, 0, -1):
    A[i] = A[i] - A[i-1]
A[0] = 0
print("价格变化：\t", A)
low, high, res = find_maximum_subarray(A, 0, len(A)-1)
print("第{}天[{}]买入, 第{}天[{}]卖出, 收益最高, 为：{}".format(low, B[low-1], high+1, B[high], res))