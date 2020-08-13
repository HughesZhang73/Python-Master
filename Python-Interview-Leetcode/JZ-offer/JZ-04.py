#coding=utf-8

from typing import List


# ===============================方法一================================
#
# def findNumberIn2DArray(matrix: List[List[int]], target: int) -> bool:
#     """
#     直接暴力搜索，不过并没有用到题目给的这个矩阵的性质
#     :param matrix:
#     :param target:
#     :return:
#     """
#
#     if len(matrix) != 0 and len(matrix[0]) != 0:
#         raw = len(matrix)
#         column = len(matrix[0])
#         for i in range(raw):
#             for j in range(column):
#                 if matrix[i][j] == target:
#                     print("found")
#                     return True
#     else:
#         print("not found")
#         return False
#
#     print("not found")
#     return False
#


# ===============================方法二================================
#
# def findNumberIn2DArray(matrix: List[List[int]], target: int) -> bool:
#     """
#     使用列或者行 是 有序的性质，这里使用行是有序的这个特点，进行二分查找 来提高效率
#     :param matrix:
#     :param target:
#     :return:
#     """
#     if len(matrix) != 0 and len(matrix[0]) != 0:
#         raw = len(matrix)
#         column = len(matrix[0])
#         for i in range(raw):
#             if binary_search(matrix[i], target):
#                 # print("found")
#                 return True
#
#     else:
#         # print("not found1")
#         return False
#
#     # print("not found2")
#     return False
#
#
# def binary_search(arr: list, key) -> bool:
#
#     head = 0
#     tail = len(arr)
#     while head < tail:
#         mid = (head + tail) >> 1
#         if key < arr[mid]:
#             tail = mid
#         elif key == arr[mid]:
#             # print("found")
#             return True
#         else:
#             head = mid + 1
    
# ===============================方法三================================
def findNumberIn2DArray(matrix: List[List[int]], target: int) -> bool:
    """
    1.该方法利用题目中所给的矩阵的性质进行求解，因为行和列都是有序排列的，所以，我们可以从第一行的最后一个元素出发，
    2.小于就往左走， 大于就往下走
    :param matrix:
    :param target:
    :return:
    """
    if len(matrix) != 0 and len(matrix[0]) != 0:
        raws = len(matrix)
        cols = len(matrix[0])
        
        raw = 0            # 控制垂直的走向
        column = cols - 1  # 控制水平的走向
        
        while raw <= raws - 1 and column >= 0:
            num = matrix[raw][column]
            if num == target:
                print("found")
                return True
            elif num > target:
                column -= 1
            else:
                raw += 1
        # print("not found")
        return False
    else:
        # print("not found")
        return False

      
    
if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    findNumberIn2DArray(matrix, 30)
    # binary_search(matrix[0], 15)
