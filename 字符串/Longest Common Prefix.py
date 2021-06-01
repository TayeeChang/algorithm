# -*- coding: utf-8 -*-
# @Time : 2021/5/19 15:16
# @Author : haojie zhang

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return strs[0][:i]

        return strs[0]

    def longestCommonPrefix1(self, strs: List[str]) -> str:
        right_most = len(strs[0])
        for i in range(1, len(strs)):
            for j in range(right_most):
                if j >= len(strs[i]) or strs[i][j] != strs[0][j]:
                    right_most = j
                    break

        return strs[0][:right_most]


strs = ["flower", "flow", "flight"]
s = Solution()
print(s.longestCommonPrefix1(strs))