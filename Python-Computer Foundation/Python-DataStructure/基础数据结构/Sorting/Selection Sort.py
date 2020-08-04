#coding=utf-8


def Selection(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i, len(arr)):  # 找后半段未排序部分最小的元素
            if arr[j] > arr[mini]:
                mini = j
            v = arr[j]
            arr[j] = arr[mini]
            arr[mini] = v
            

if __name__ == '__main__':
    arr = [1, 3, 4, 54, 4, 7, 8]
    Selection(arr)
    print(arr)
