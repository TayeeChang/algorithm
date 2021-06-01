# -*- coding: utf-8 -*-
# @Time : 2021/5/17 11:23
# @Author : haojie zhang

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for i in range(n):
            for j in range(n-1-i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]

        for i in range(n//2):
            for j in range(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

        return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
print(s.rotate(matrix))