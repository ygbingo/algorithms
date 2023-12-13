from insertion_sort import sort
# from merge_sort import sort

A = [2, 3, 4, 1, 6, 8, 9, 0]
print("before sort: ")
print(A)

print("after sort: ")
sort(A)
print(A)

print("after reverse sort: ")
sort(A, reverse=True)
print(A)