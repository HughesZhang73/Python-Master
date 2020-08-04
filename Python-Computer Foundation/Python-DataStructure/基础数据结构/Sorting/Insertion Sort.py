# coding=utf-8
from typing import List


def insertion_Sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':
    arr = [1, 3, 4, 54, 4, 7, 8]
    insertion_Sort(arr)
    print(arr)
