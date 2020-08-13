#coding=utf-8
"""
二分查找的列表必须是有序才行

"""


def binary_search(arr, key):
    head = 0
    tail = len(arr) - 1
    while head < tail:
        mid = (head + tail) >> 1
        if key == arr[mid]:
            print("found")
            return 1
        elif key < arr[mid]:
            tail = mid
        else:
            head = mid + 1
    print("not found")
    return 0


if __name__ == '__main__':
    arr = [1, 3, 4, 55, 66, 77]
    binary_search(arr, 1)
