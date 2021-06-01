# -*- coding: utf-8 -*-
# @Time : 2021/5/31 15:34
# @Author : haojie zhang


from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def traceback(index):
            if index == n:
                res.append(used[:])
                return
            for j in range(n):
                if isvalid(index, j, used):
                    used[index] = j
                    traceback(index+1)
            return

        def isvalid(index, j, used):
            for row in range(index):
                if used[row] == j or abs(index - row) == abs(j - used[row]):
                    return False
            return True

        def printNQueens(res):
            s = []
            for i in range(len(res)):
                t = [['.'] * n for _ in range(n)]
                for row, col in enumerate(res[i]):
                    t[row][col] = 'Q'
                s.append([''.join(l) for l in t])
            return s

        res = []
        used = [0] * n
        traceback(0)
        return printNQueens(res)


n = 4
s = Solution()
print(s.solveNQueens(n))
