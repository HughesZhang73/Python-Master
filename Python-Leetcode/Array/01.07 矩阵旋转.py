# coding=utf-8
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        new_matrix = [[0] * n for i in range(n)]
        
        for j in range(n):
            for x in range(n):
                new_matrix[j][x] = matrix[n - 1 - x][j]
        
        matrix[:] = new_matrix[:]
        

# 时间最短解法
class Solution1:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 先上下镜面翻转
        # for i in range(n // 2):
        #     for j in range(n):
        #         matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]
        #
        
        matrix[:] = matrix[::-1] # 进行上下镜面反转的代码功能相同
        
        
        # 再主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]