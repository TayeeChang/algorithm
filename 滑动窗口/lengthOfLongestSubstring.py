# -*- coding: utf-8 -*-
# @Time : 2021/4/25 14:23
# @Author : haojie zhang

# 3. 无重复字符的最长子串

"""
3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        window = defaultdict(int)
        res = 0
        left = right = 0  # [left, right) 开区间
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            while window[c] > 1:
                t = s[left]
                left += 1
                window[t] -= 1
            res = max(res, right-left)  # [left, right) 开区间
        return res


s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
