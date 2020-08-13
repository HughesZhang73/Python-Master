#coding=utf-8

"""
线性搜索中引入标记之后，可以将搜索的效率提高常数倍
"""


def linear_search(arr: list, key) -> bool:
    i = 0
    print(arr[i])
    while arr[i] != key:
        i += 1
    print(i)
    return i != len(arr) - 1


if __name__ == '__main__':
    arr = [1, 2, 4, 3, 7, 44, 45, 4325]
    if linear_search(arr, 432):
        print("found")
    else:
        print("not found")
