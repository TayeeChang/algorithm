# -*- coding: utf-8 -*-
# @Time : 2021/5/4 15:00
# @Author : haojie zhang


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def traceback(n, k, index, tmp):
            if k == 0:
                res.append(tmp)
                return
            for i in range(index, n+1):
                traceback(n, k-1, i+1, tmp+[i])

        res = []
        traceback(n, k, 1, [])
        return res