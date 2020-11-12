# coding=utf-8


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        ans = [[0]*n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if matrix[m][n] == 0:
                    piv_row, piv_col = m, n
