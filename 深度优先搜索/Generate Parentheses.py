# -*- coding: utf-8 -*-
# @Time : 2021/5/31 17:45
# @Author : haojie zhang

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(n, left, right, tmp):
            if left == n and right == n:
                res.append(tmp)
                return
            if left < n:
                dfs(n, left+1, right, tmp+'(')
            if right < left:
                dfs(n, left, right+1, tmp+')')

        res = []
        dfs(n, 0, 0, '')
        return res


n = 1
s = Solution()
print(s.generateParenthesis(n))
