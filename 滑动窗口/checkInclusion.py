# -*- coding: utf-8 -*-
# @Time : 2021/4/25 10:23
# @Author : haojie zhang

# 字符串的排列

"""
567. 字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的 子串 。
https://leetcode-cn.com/problems/permutation-in-string/
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        need = defaultdict(int)
        window = defaultdict(int)
        res = False
        valid = 0
        for c in s1:
            need[c] += 1
        left, right = 0, 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if right - left == len(s1):
                    return True
                c = s2[left]
                left += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return False


s1 = "ab"
s2 = "eidboaoo"
s = Solution()
print(s.checkInclusion(s1, s2))



