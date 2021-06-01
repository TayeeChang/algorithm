# -*- coding: utf-8 -*-
# @Time : 2021/5/17 14:11
# @Author : haojie zhang

from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        c = 2 ** (n-1)
        res = self.grayCode(n-1)
        for t in reversed(res):
            res.append(c + t)
        return res


n = 3
s = Solution()
print(s.grayCode(n))