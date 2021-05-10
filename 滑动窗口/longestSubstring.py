# -*- coding: utf-8 -*-
# @Time : 2021/5/5 13:28
# @Author : haojie zhang

"""
395. 至少有 K 个重复字符的最长子串
给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。
https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/


示例 1：

输入：s = "aaabb", k = 3
输出：3
解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
示例 2：

输入：s = "ababbc", k = 2
输出：5
解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        from collections import defaultdict
        maxUnique = 0
        dic = {}
        for c in s:
            if c not in dic:
                maxUnique += 1
                dic[c] = 1
        res = 0
        for currUnique in range(1, maxUnique+1):
            left = right = 0
            unique, leastK = 0, 0
            memo = defaultdict(int)
            while right < len(s):
                if unique <= currUnique:
                    ch = s[right]
                    right += 1
                    memo[ch] += 1
                    if memo[ch] == 1:
                        unique += 1
                    if memo[ch] == k:
                        leastK += 1
                else:
                    t = s[left]
                    left += 1
                    if memo[t] == 1:
                        unique -= 1
                    if memo[t] == k:
                        leastK -= 1
                    memo[t] -= 1

                if unique == currUnique and leastK == currUnique:
                    res = max(res, right - left)
        return res


s= "aaabbb"
k = 3
obj = Solution()
print(obj.longestSubstring(s, k))
