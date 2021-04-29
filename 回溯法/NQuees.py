# -*- coding: utf-8 -*-
# @Time : 2021/4/29 9:44
# @Author : haojie zhang

"""
def backtrack(path, selected):
    if 满足停止条件：
        res.append(path)
    for 选择 in 选择列表：
        做出选择
        递归执行backtrack
        撤销选择
"""


class Solution:
    def totalNQueens(self, n: int) -> int:

        def traceback(n, index):
            if index == n:
                nonlocal res
                res += 1
                return
            for j in range(n):
                if not isvalid(index, j):
                    continue
                used[index] = j
                traceback(n, index+1)
                used[index] = 0

        def isvalid(index, j):
            for i in range(index):
                if used[i] == j or abs(index-i) == abs(j-used[i]):
                    return False
            return True

        used = [0] * n
        res = 0
        traceback(n, 0)
        return res


s = Solution()
n = 15
print(s.totalNQueens(n))




