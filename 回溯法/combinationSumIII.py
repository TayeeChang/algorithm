# -*- coding: utf-8 -*-
# @Time : 2021/4/29 16:48
# @Author : haojie zhang

from typing import List

"""
216. 组合总和 III
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def traceback(n, k, sums, index, tmp):
            if k == 0 and sums == n:
                res.append(tmp)
                return
            for i in range(index, 10):
                if sums + i > n:
                    break
                traceback(n, k-1, sums+i, i+1, tmp+[i])
        res = []
        traceback(n, k, 0, 1, [])
        return res

