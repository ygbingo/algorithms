"""
堆排序
worst: O(nlgn)
"""
import math


def buildMaxHeap(arr, reverse):
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr, i, reverse)

def heapify(arr, i, reverse=False):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and (arr[left] > arr[largest] if not reverse else arr[left] < arr[largest]):
        largest = left
    if right < arrLen and (arr[right] > arr[largest] if not reverse else arr[right] < arr[largest]):
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def sort(arr, reverse=False):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr, reverse)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen -=1
        heapify(arr, 0)
    return arr

