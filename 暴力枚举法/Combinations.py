# -*- coding: utf-8 -*-
# @Time : 2021/6/2 14:51
# @Author : haojie zhang

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def dfs(n, k, index, tmp):
            if k == 0:
                res.append(tmp)
                return
            for i in range(index, n+1):
                dfs(n, k-1, i+1, tmp+[i])

        res = []
        dfs(n, k, 1, [])
        return res

n = 4
k = 2
s = Solution()
print(s.combine(n, k))