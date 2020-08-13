#coding=utf-8


L = []
R = []


def merge(arr: list, n: int, l: int, m: int, r: int):
    n1 = m - l
    n2 = r - m
    
    for i in range(n1):
        L.append(arr[l + i])
    
    for i in range(n2):
        R.append(arr[m + i])
    
    # 进行两个数组之间的合并
    
    # L.insert(n1, 20000000000)
    # R.insert(n2, 20000000000)
    
    print(L)
    print(R)
    #
    
    l_p = r_p = 0  # 合并左右数组的左右指针， 分别指向两个数组的第一个位置（下标为0）
    
    for x in range(l, r):
        if L[l_p] <= R[r_p]:
            arr[x] = L[l_p]
            l_p += 1
        else:
            arr[x] = R[r_p]
            r_p += 1
            
    
def merge_sort(arr: list, n: int, left: int, right: int) -> list:
    if left < right - 1:
        mid = (left + right) >> 1
        merge_sort(array, n, left, mid)
        merge_sort(array, n, mid, right)
        merge(arr, n, left, mid, right)
    return arr


if __name__ == '__main__':
    array = [9, 6, 7, 2, 5, 1, 8, 4, 2]
    print(merge_sort(array, len(array), 0, len(array)))
