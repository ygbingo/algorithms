"""
最大子数组问题, 股票最高收益问题
"""


def find_max_crossing_subarray(A, low, mid, high):
    left_sum = 0
    sub_sum = 0
    max_left = mid
    for i in range(mid, low-1, -1):
        sub_sum += A[i]
        if sub_sum > left_sum:
            left_sum = sub_sum
            max_left = i 
    right_sum = 0
    sub_sum = 0
    max_right = mid
    for j in range(mid+1, high):
        sub_sum += A[j]
        if sub_sum > right_sum:
            right_sum = sub_sum
            max_right = j
    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(A, low, high):
    if low == high:
        return low, high, A[low]
    else:
        mid = int((low+high)/2)
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum