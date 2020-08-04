# coding=utf-8


def Bouble_Sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr) - 1):
            # if arr[j] > arr[j + 1]:
            #     temp = arr[j]
            #     arr[j] = arr[j + 1]
            #     arr[j + 1] = temp
            switch(arr, j, j + 1)
            
            
def switch(arr, a, b):
    if arr[a] > arr[b]:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
    return


if __name__ == '__main__':
    arr = [1, 3, 41, 54, 42, 7, 8]
    Bouble_Sort(arr)
    x = print(arr)
