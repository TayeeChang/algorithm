# -*- coding: utf-8 -*-
# @Time : 2021/4/29 10:01
# @Author : haojie zhang

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List:

        def traceback(n, index):
            if index == n:
                res.append(help(n))
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

        def help(n):
            s = [['.'] * n for _ in range(n)]
            for i in range(n):
                s[i][used[i]] = 'Q'
            for i in range(n):
                s[i] = ''.join(s[i])
            return s

        used = [0] * n
        res = []
        traceback(n, 0)
        return res

n = 4
s = Solution()
print(s.solveNQueens(n))





